# 01_measurement_cfa_invariance.R — CFA, reliability/AVE, measurement invariance
# Establish construct validity BEFORE substantive tests (a JAP gate).
# lavaan path is guarded; a base-R Cronbach's alpha runs without it.
# Source 00_setup.R first.

if (!exists("dat")) source(file.path("R", "00_setup.R"))

## ---- base-R reliability (always runs) ---------------------------------------
cronbach_alpha <- function(items) {
  items <- as.matrix(items); k <- ncol(items)
  v_items <- sum(apply(items, 2, var))
  v_total <- var(rowSums(items))
  (k / (k - 1)) * (1 - v_items / v_total)
}
cat("== Cronbach's alpha (base R) ==\n")
cat(sprintf("  X scale: %.3f\n", cronbach_alpha(dat[, c("x1","x2","x3")])))
cat(sprintf("  M scale: %.3f\n", cronbach_alpha(dat[, c("m1","m2","m3")])))

## ---- CFA + omega/AVE + invariance (lavaan) ----------------------------------
if (!requireNamespace("lavaan", quietly = TRUE)) {
  message("\nlavaan not installed — skipping CFA/invariance.\n",
          "Install: install.packages(c('lavaan','semTools'))")
} else {
  suppressPackageStartupMessages(library(lavaan))

  cfa_model <- '
    Xlat =~ x1 + x2 + x3
    Mlat =~ m1 + m2 + m3
  '
  fit <- cfa(cfa_model, data = dat, std.lv = TRUE)
  cat("\n== CFA fit ==\n")
  print(fitMeasures(fit, c("chisq","df","pvalue","cfi","tli","rmsea","srmr")))

  # Composite reliability (omega) and AVE from standardized loadings
  std <- standardizedSolution(fit)
  load <- std[std$op == "=~", ]
  for (lv in unique(load$lhs)) {
    l <- load$est.std[load$lhs == lv]
    omega <- sum(l)^2 / (sum(l)^2 + sum(1 - l^2))
    ave   <- mean(l^2)
    cat(sprintf("  %s: omega(CR)=%.3f  AVE=%.3f\n", lv, omega, ave))
  }

  # Measurement invariance across groups: configural -> metric -> scalar
  if (requireNamespace("semTools", quietly = TRUE)) {
    cat("\n== measurement invariance (configural/metric/scalar) ==\n")
    conf <- cfa(cfa_model, data = dat, group = "group", std.lv = TRUE)
    metr <- cfa(cfa_model, data = dat, group = "group",
                group.equal = "loadings", std.lv = TRUE)
    scal <- cfa(cfa_model, data = dat, group = "group",
                group.equal = c("loadings","intercepts"), std.lv = TRUE)
    print(anova(conf, metr, scal))
    cat("Rule of thumb: invariance holds if dCFI <= .010 and dRMSEA <= .015.\n")
  }
}
