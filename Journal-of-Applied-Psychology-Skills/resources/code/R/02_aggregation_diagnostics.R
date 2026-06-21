# 02_aggregation_diagnostics.R — ICC(1), ICC(2), r_wg(j)
# Justify (or refuse) aggregating an individual measure to the team level.
# JAP referees will not accept a team-level construct without these.
# Source 00_setup.R first.

if (!exists("dat")) source(file.path("R", "00_setup.R"))

## ---- ICC(1) and ICC(2) from a random-intercept model ------------------------
# ICC(1): proportion of variance between teams (is there a group effect at all?)
# ICC(2): reliability of the TEAM MEAN (depends on ICC1 and team size)
icc12 <- function(y, group) {
  group <- factor(group)
  if (requireNamespace("lme4", quietly = TRUE)) {
    m  <- lme4::lmer(y ~ 1 + (1 | group))
    vc <- as.data.frame(lme4::VarCorr(m))
    tau2 <- vc$vcov[vc$grp == "group"]; sig2 <- vc$vcov[vc$grp == "Residual"]
  } else {                                  # one-way ANOVA fallback
    a <- anova(lm(y ~ group)); msb <- a$`Mean Sq`[1]; msw <- a$`Mean Sq`[2]
    k <- mean(table(group)); tau2 <- (msb - msw) / k; sig2 <- msw
  }
  icc1 <- tau2 / (tau2 + sig2)
  kbar <- mean(table(group))
  icc2 <- (kbar * icc1) / (1 + (kbar - 1) * icc1)   # Spearman-Brown form
  c(ICC1 = icc1, ICC2 = icc2, k_bar = kbar)
}

cat("== aggregation diagnostics for X (climate) ==\n")
print(round(icc12(dat$X, dat$team), 3))
cat("\nGuidance: ICC(1) ~ .05/.10/.25 = small/medium/large group effect;\n",
    "ICC(2) >= .70 supports using the team mean as a reliable unit-level score.\n")

## ---- r_wg(j) within-group agreement -----------------------------------------
# Agreement of a J-item scale within each group vs a uniform null.
# Here we treat the 3 X indicators as a J=3 scale on a 1-7 response metric.
rwgj <- function(items, J = ncol(items), A = 7) {
  sig2_eu <- (A^2 - 1) / 12                 # expected variance under uniform null
  sx2 <- mean(apply(items, 2, var))         # mean observed item variance
  num <- J * (1 - sx2 / sig2_eu)
  num / (num + (sx2 / sig2_eu))
}
# rescale synthetic indicators to a 1-7 metric for the demo
to17 <- function(z) round(pmin(pmax(scale(z) * 1.2 + 4, 1), 7))
agree <- tapply(seq_len(nrow(dat)), dat$team, function(idx) {
  its <- cbind(to17(dat$x1[idx]), to17(dat$x2[idx]), to17(dat$x3[idx]))
  rwgj(its)
})
cat(sprintf("\nr_wg(j): median = %.3f across %d teams (>= .70 supports aggregation)\n",
            median(agree, na.rm = TRUE), length(agree)))
