# 02_model_comparison_recovery.R — formal model fitting, comparison, and recovery
# Cognitive Psychology rewards a FITTED model that beats a rival AND is recoverable.
# Pure base R (stats::optim); runnable on a stock install. Source 00_setup.R first.

if (!exists("dat")) source(file.path("R", "00_setup.R"))
set.seed(20260621)

## ---- a toy "cognitive model": condition-wise RT as a shifted-lognormal -------
# M1 (full):    separate mu per condition, shared sigma + shift  (3 params)
# M0 (reduced): single mu across conditions                      (2 params)
# Likelihood of observed RT given shift t0 (non-decision floor).
negll <- function(par, rt, x, full = TRUE) {
  t0 <- plogis(par[1]) * 150            # non-decision shift in (0,150) ms
  sigma <- exp(par[2])
  if (full) { mu <- par[3] + par[4] * x } else { mu <- par[3] }
  resid <- rt - t0
  if (any(resid <= 0)) return(1e10)
  -sum(dlnorm(resid, meanlog = mu, sdlog = sigma, log = TRUE))
}

fit_model <- function(rt, x, full = TRUE) {
  start <- if (full) c(0, log(0.25), 6.2, 0.1) else c(0, log(0.25), 6.2)
  optim(start, negll, rt = rt, x = x, full = full,
        method = "Nelder-Mead", control = list(maxit = 2000))
}

x <- as.integer(dat$cond == "incongruent")
f1 <- fit_model(dat$rt, x, full = TRUE)
f0 <- fit_model(dat$rt, x, full = FALSE)

ic <- function(fit, k, n) c(AIC = 2 * fit$value + 2 * k,
                            BIC = 2 * fit$value + k * log(n))
n  <- nrow(dat)
tab <- rbind(M1_full = ic(f1, 4, n), M0_reduced = ic(f0, 3, n))
cat("== model comparison (lower is better) ==\n"); print(round(tab, 1))

# BIC approximation to the Bayes factor for M1 over M0 (Wagenmakers, 2007)
bf10 <- exp((tab["M0_reduced", "BIC"] - tab["M1_full", "BIC"]) / 2)
cat(sprintf("\nBIC-approx Bayes factor BF10 (full vs reduced) = %.2f\n", bf10))

## ---- parameter recovery -----------------------------------------------------
# Simulate from known params, refit, check we recover the congruency effect.
recover_one <- function(true_eff) {
  t0 <- 100; sigma <- 0.25; mu0 <- 6.2
  xx <- rep(0:1, each = 600)
  rt <- t0 + rlnorm(length(xx), mu0 + true_eff * xx, sigma)
  fit_model(rt, xx, full = TRUE)$par[4]
}
true_effs <- rep(c(0.05, 0.15, 0.25), each = 20)
est <- vapply(true_effs, recover_one, numeric(1))
rec <- aggregate(est, list(true = true_effs), function(z) c(mean = mean(z), sd = sd(z)))
cat("\n== parameter recovery (estimated congruency effect by true value) ==\n")
print(do.call(rbind, lapply(seq_len(nrow(rec)),
      function(r) data.frame(true = rec$true[r],
                             mean_est = round(rec$x[r, "mean"], 3),
                             sd_est = round(rec$x[r, "sd"], 3)))))
cat(sprintf("recovery correlation r(true, est) = %.3f\n", cor(true_effs, est)))

## ---- model recovery ---------------------------------------------------------
# Simulate from each model, refit BOTH, count how often AIC picks the generator.
sim_pick <- function(generator_full) {
  xx <- rep(0:1, each = 600)
  eff <- if (generator_full) 0.15 else 0
  rt  <- 100 + rlnorm(length(xx), 6.2 + eff * xx, 0.25)
  a1 <- ic(fit_model(rt, xx, TRUE), 4, length(xx))["AIC"]
  a0 <- ic(fit_model(rt, xx, FALSE), 3, length(xx))["AIC"]
  if (a1 < a0) "M1_full" else "M0_reduced"
}
gen_full <- replicate(30, sim_pick(TRUE))
gen_red  <- replicate(30, sim_pick(FALSE))
cm <- rbind(`gen=M1` = table(factor(gen_full, c("M1_full", "M0_reduced"))),
            `gen=M0` = table(factor(gen_red,  c("M1_full", "M0_reduced"))))
cat("\n== model-recovery confusion matrix (rows=generator, cols=selected) ==\n")
print(cm)
