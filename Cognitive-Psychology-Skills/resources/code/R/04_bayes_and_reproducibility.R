# 04_bayes_and_reproducibility.R — hierarchical Bayes + transparency discipline
# The hierarchical-Bayes path for the same design, plus a robustness sweep and a
# reproducibility footer. brms/Stan are heavy; this script GUARDS them and still
# runs its sensitivity + sessionInfo sections on a stock install.
# Source 00_setup.R first.

if (!exists("dat")) source(file.path("R", "00_setup.R"))

## ---- hierarchical Bayesian LMM (brms / Stan) --------------------------------
if (requireNamespace("brms", quietly = TRUE)) {
  suppressPackageStartupMessages(library(brms))
  # Weakly-informative priors; report them. Shifted-lognormal family fits RTs well.
  priors <- c(set_prior("normal(0, 0.5)", class = "b"),
              set_prior("student_t(3, 0, 0.3)", class = "sd"))
  fit <- brm(rt ~ c_cond + (1 + c_cond | subj) + (1 | item),
             data = dat, family = shifted_lognormal(),
             prior = priors, chains = 4, cores = 4,
             iter = 2000, seed = 20260621, refresh = 0)
  print(summary(fit))
  if (requireNamespace("loo", quietly = TRUE)) {
    cat("\n== LOO (compare against a reduced model for model selection) ==\n")
    print(loo(fit))
  }
} else {
  message("brms not installed — skipping the Bayesian fit.\n",
          "Install: install.packages('brms') (pulls Stan via cmdstanr/rstan).")
}

## ---- robustness: outlier-exclusion sensitivity sweep ------------------------
# Report whether the congruency RT cost survives reasonable cleaning choices.
rt_cost <- function(d) {
  agg <- aggregate(rt ~ subj + cond, data = d, FUN = mean)
  w <- reshape(agg, idvar = "subj", timevar = "cond", direction = "wide")
  mean(w$`rt.incongruent` - w$`rt.congruent`)
}
rules <- list(
  none          = dat,
  drop_lt_250   = dat[dat$rt > 250, ],
  drop_gt_2500  = dat[dat$rt < 2500, ],
  trim_2.5sd    = dat[abs(scale(dat$log_rt)) < 2.5, ],
  correct_only  = dat[dat$acc == 1, ]
)
cat("\n== sensitivity of the RT cost (ms) to exclusion rules ==\n")
for (nm in names(rules))
  cat(sprintf("  %-14s n=%5d  cost=%6.1f ms\n",
              nm, nrow(rules[[nm]]), rt_cost(rules[[nm]])))

## ---- reproducibility footer -------------------------------------------------
cat("\n== reproducibility ==\nseed: 20260621\n")
cat("R:", R.version.string, "\n")
loaded <- intersect(c("lme4","lmerTest","emmeans","effectsize","brms","loo"),
                    rownames(installed.packages()))
if (length(loaded))
  print(sapply(loaded, function(p) as.character(packageVersion(p))))
# In a real project: pin with renv::snapshot(); deposit data+code+seed (OSF/Zenodo);
# confirm a fresh-session run regenerates every fit, figure, and table.
