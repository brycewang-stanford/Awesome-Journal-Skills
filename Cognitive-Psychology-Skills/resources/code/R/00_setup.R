# 00_setup.R — packages, seed, and a synthetic trial-level dataset
# Cognitive Psychology code kit. Source this first; it defines `dat` and helpers.
# Runnable on a stock R install (verified on R 4.5.2, 2026-06).

set.seed(20260621)  # report the seed in the manuscript; deposits must regenerate from it

## ---- optional packages (guarded; scripts degrade to base R if absent) --------
have <- function(pkg) requireNamespace(pkg, quietly = TRUE)
opt  <- c("lme4", "lmerTest", "emmeans", "effectsize", "brms", "loo")
for (p in opt) if (!have(p)) message("optional package not installed: ", p)

## ---- synthetic trial-level data ---------------------------------------------
# A within-subject 2-condition cognitive experiment with CROSSED subject & item
# random effects — the structure that forces a mixed model rather than aggregating
# to per-subject means. RT in ms (lognormal); accuracy Bernoulli.
n_subj  <- 40
n_item  <- 24            # each item seen in both conditions (fully crossed)
conds   <- c("congruent", "incongruent")

subj_re <- rnorm(n_subj, 0, 0.18)            # subject log-RT intercept
subj_sl <- rnorm(n_subj, 0, 0.08)            # subject congruency slope
item_re <- rnorm(n_item, 0, 0.10)            # item log-RT intercept

grid <- expand.grid(subj = factor(seq_len(n_subj)),
                    item = factor(seq_len(n_item)),
                    cond = factor(conds, levels = conds),
                    KEEP.OUT.ATTRS = FALSE, stringsAsFactors = TRUE)

x_incong <- as.integer(grid$cond == "incongruent")   # 0/1 effect-coded below too
s <- as.integer(grid$subj); i <- as.integer(grid$item)

# log-RT model: grand mean 6.4 (~600 ms) + 0.12 congruency cost + random effects
mu_logrt <- 6.40 + 0.12 * x_incong +
            subj_re[s] + subj_sl[s] * x_incong + item_re[i]
grid$rt  <- round(exp(mu_logrt + rnorm(nrow(grid), 0, 0.22)))   # residual log-SD

# accuracy: higher for congruent; logistic with subject random intercept
eta_acc  <- 2.2 - 0.6 * x_incong + 0.9 * subj_re[s]
grid$acc <- rbinom(nrow(grid), 1, plogis(eta_acc))

# light, pre-registered cleaning: drop impossibly fast RTs on correct trials only
grid$keep <- with(grid, rt > 200 & rt < 3000)
dat <- grid[grid$keep, c("subj", "item", "cond", "rt", "acc")]
dat$log_rt  <- log(dat$rt)
dat$c_cond  <- ifelse(dat$cond == "incongruent", 0.5, -0.5)  # centered/effect-coded

cat(sprintf("dat: %d trials, %d subjects, %d items; mean RT %.0f ms; accuracy %.2f\n",
            nrow(dat), nlevels(dat$subj), nlevels(dat$item),
            mean(dat$rt), mean(dat$acc)))

## ---- small helpers ----------------------------------------------------------
# d_z for a within-subject contrast from per-subject condition means
cohen_dz <- function(x1, x2) {
  d <- x1 - x2
  mean(d) / sd(d)
}
invisible(TRUE)
