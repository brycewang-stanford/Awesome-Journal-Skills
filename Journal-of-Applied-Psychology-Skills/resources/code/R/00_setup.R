# 00_setup.R — packages, seed, and synthetic NESTED data for I-O psychology
# Journal of Applied Psychology code kit. Source this first.
# Runnable on a stock R install (verified on R 4.5.2, 2026-06).

set.seed(20260621)  # report the seed; deposits must regenerate from it

have <- function(pkg) requireNamespace(pkg, quietly = TRUE)
for (p in c("lme4", "lavaan", "semTools", "psych", "metafor"))
  if (!have(p)) message("optional package not installed: ", p)

## ---- multilevel data: employees nested in teams -----------------------------
# X (e.g., leadership), M (e.g., engagement), Y (e.g., performance), measured at
# the individual level with team-level variance — the canonical JAP structure.
n_team   <- 50
team_n   <- sample(6:14, n_team, replace = TRUE)     # unequal team sizes
N        <- sum(team_n)
team     <- factor(rep(seq_len(n_team), times = team_n))

u_team   <- rnorm(n_team, 0, 0.45)                   # team random intercept (Y)
u_x      <- rnorm(n_team, 0, 0.40)                   # team-level X shift (climate)

X  <- 0.5 * u_x[as.integer(team)] + rnorm(N, 0, 0.9) # individual X with team share
a  <- 0.45; b <- 0.40; cp <- 0.15                    # true a, b, c' paths
M  <- 0.0 + a * X + rnorm(N, 0, 0.9)
Y  <- 0.0 + cp * X + b * M + u_team[as.integer(team)] + rnorm(N, 0, 0.9)

dat <- data.frame(team, X, M, Y)

## ---- multi-indicator latent measurement (3 indicators each) -----------------
# Indicators load on the latent; lets 01 fit a CFA and compute omega/AVE.
make_ind <- function(eta, loadings, err_sd = 0.55) {
  sapply(loadings, function(l) l * eta + rnorm(length(eta), 0, err_sd))
}
ind_X <- make_ind(scale(X), c(0.80, 0.75, 0.70))
ind_M <- make_ind(scale(M), c(0.78, 0.72, 0.68))
colnames(ind_X) <- paste0("x", 1:3); colnames(ind_M) <- paste0("m", 1:3)
dat <- cbind(dat, ind_X, ind_M)
dat$group <- factor(rep(c("A", "B"), length.out = N))   # for invariance demo

cat(sprintf("dat: N=%d employees in %d teams (sizes %d-%d)\n",
            N, n_team, min(team_n), max(team_n)))

## ---- effect-size table for the meta-analysis script -------------------------
# k independent studies: observed correlation r_obs and the reliabilities of the
# two measures (artifact information for psychometric correction).
k <- 18
rho_true <- 0.30
rel_x <- runif(k, 0.70, 0.92); rel_y <- runif(k, 0.70, 0.92)
n_i   <- sample(80:400, k, replace = TRUE)
r_true_i <- rho_true + rnorm(k, 0, 0.05)                      # true heterogeneity
r_obs <- r_true_i * sqrt(rel_x * rel_y) + rnorm(k, 0, 0.04)   # attenuated + samp. err
meta_tab <- data.frame(study = seq_len(k), n = n_i,
                       r_obs = round(pmin(pmax(r_obs, -.99), .99), 3),
                       rel_x = round(rel_x, 3), rel_y = round(rel_y, 3))

invisible(TRUE)
