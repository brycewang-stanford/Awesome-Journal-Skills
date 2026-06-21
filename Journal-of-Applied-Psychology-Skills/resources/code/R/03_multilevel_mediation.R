# 03_multilevel_mediation.R — multilevel model + 1-1-1 mediation with MC CI
# JAP wants MODEL-BASED indirect effects with confidence intervals, with the
# within- and between-team parts separated by group-mean centering.
# Source 00_setup.R first.

if (!exists("dat")) source(file.path("R", "00_setup.R"))

if (!requireNamespace("lme4", quietly = TRUE)) {
  stop("lme4 required: install.packages('lme4')")
}
suppressPackageStartupMessages(library(lme4))

## ---- group-mean centering (separate within vs between effects) ---------------
gm <- function(x, g) ave(x, g, FUN = mean)
dat$X_b <- gm(dat$X, dat$team); dat$X_w <- dat$X - dat$X_b
dat$M_b <- gm(dat$M, dat$team); dat$M_w <- dat$M - dat$M_b

## ---- a-path (X -> M) and b/c'-path (M,X -> Y), random intercepts -------------
m_a <- lmer(M ~ X_w + X_b + (1 | team), data = dat, REML = FALSE)
m_b <- lmer(Y ~ M_w + M_b + X_w + X_b + (1 | team), data = dat, REML = FALSE)

a_w  <- fixef(m_a)["X_w"];  b_w  <- fixef(m_b)["M_w"]
se_a <- sqrt(vcov(m_a)["X_w","X_w"]); se_b <- sqrt(vcov(m_b)["M_w","M_w"])
ind_w <- a_w * b_w

cat("== within-team paths ==\n")
cat(sprintf("  a (X_w->M)  = %.3f (SE %.3f)\n", a_w, se_a))
cat(sprintf("  b (M_w->Y)  = %.3f (SE %.3f)\n", b_w, se_b))
cat(sprintf("  c' (X_w->Y) = %.3f\n", fixef(m_b)["X_w"]))
cat(sprintf("  indirect a*b = %.3f\n", ind_w))

## ---- Monte-Carlo confidence interval for the indirect effect ----------------
# Draw a, b from their sampling distributions; take quantiles of a*b.
# (The asymmetric, model-based alternative to a Sobel z; cf. bootstrap.)
set.seed(20260621)
draws <- 20000
a_s <- rnorm(draws, a_w, se_a); b_s <- rnorm(draws, b_w, se_b)
mc  <- quantile(a_s * b_s, c(.025, .975))
cat(sprintf("\nMonte-Carlo 95%% CI for indirect effect: [%.3f, %.3f]\n", mc[1], mc[2]))
cat("Significant if the CI excludes 0. Report this, not a causal-steps p-value.\n")

## ---- nonparametric bootstrap cross-check ------------------------------------
boot_ind <- function() {
  teams <- levels(dat$team)
  bs <- dat[dat$team %in% sample(teams, length(teams), replace = TRUE), ]
  fa <- lmer(M ~ X_w + X_b + (1 | team), data = bs, REML = FALSE)
  fb <- lmer(Y ~ M_w + M_b + X_w + X_b + (1 | team), data = bs, REML = FALSE)
  unname(fixef(fa)["X_w"] * fixef(fb)["M_w"])
}
bvals <- suppressWarnings(replicate(200, tryCatch(boot_ind(), error = function(e) NA)))
bci <- quantile(bvals, c(.025, .975), na.rm = TRUE)
cat(sprintf("Cluster-bootstrap 95%% CI (200 reps): [%.3f, %.3f]\n", bci[1], bci[2]))
