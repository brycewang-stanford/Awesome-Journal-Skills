# 04_psychometric_meta.R — psychometric meta-analysis with artifact correction
# I-O synthesis corrects observed correlations for UNRELIABILITY before pooling,
# then reports the random-effects mean, heterogeneity, and a credibility interval.
# Source 00_setup.R first.

if (!exists("meta_tab")) source(file.path("R", "00_setup.R"))

## ---- artifact correction: disattenuate each r -------------------------------
# r_corrected = r_obs / sqrt(rel_x * rel_y); the SE is inflated by the same factor.
mt <- meta_tab
mt$A  <- sqrt(mt$rel_x * mt$rel_y)          # combined attenuation factor
mt$rc <- mt$r_obs / mt$A
# sampling variance of the OBSERVED r (Fisher-z handled by metafor below);
# here use the standard var of r and inflate for the correction.
mt$var_obs <- (1 - mt$r_obs^2)^2 / (mt$n - 1)
mt$var_rc  <- mt$var_obs / mt$A^2

cat("== bare-bones vs artifact-corrected mean r ==\n")
w  <- 1 / mt$var_obs
cat(sprintf("  sample-size-weighted observed r-bar = %.3f\n",
            sum(mt$r_obs * mt$n) / sum(mt$n)))
cat(sprintf("  artifact-corrected rho-hat (mean)   = %.3f\n",
            sum(mt$rc * w) / sum(w)))

## ---- random-effects pooling (metafor on corrected r) ------------------------
if (!requireNamespace("metafor", quietly = TRUE)) {
  message("metafor not installed: install.packages('metafor')")
} else {
  suppressPackageStartupMessages(library(metafor))
  # Fisher-z transform the corrected correlations for the RE model.
  es <- escalc(measure = "ZCOR", ri = pmin(pmax(mt$rc, -.99), .99), ni = mt$n)
  re <- rma(yi, vi, data = es, method = "REML")
  rho_hat <- transf.ztor(coef(re))
  ci_lo   <- transf.ztor(re$ci.lb); ci_hi <- transf.ztor(re$ci.ub)
  cat("\n== random-effects meta-analysis (Fisher-z, back-transformed) ==\n")
  cat(sprintf("  rho-hat = %.3f, 95%% CI [%.3f, %.3f]\n", rho_hat, ci_lo, ci_hi))
  cat(sprintf("  tau^2 = %.4f   I^2 = %.1f%%   Q(%d) = %.1f, p = %.3f\n",
              re$tau2, re$I2, re$k - 1, re$QE, re$QEp))

  # 80% credibility interval (Hunter-Schmidt): where 80% of TRUE rho's lie.
  tau_r <- sd(mt$rc)                          # SD of corrected r as a simple proxy
  cr <- rho_hat + c(-1, 1) * qnorm(.90) * sqrt(max(re$tau2, 0))
  cat(sprintf("  80%% credibility interval (z-metric) approx [%.3f, %.3f]\n",
              transf.ztor(cr[1]), transf.ztor(cr[2])))
  cat("Wide credibility interval => search for moderators (meta-regression).\n")
}
