# 03_signal_detection_ddm.R — signal-detection theory + EZ-diffusion
# Decompose RT+accuracy into interpretable latent quantities, not just mean RT.
# Pure base R; runnable on a stock install. Source 00_setup.R first.

if (!exists("dat")) source(file.path("R", "00_setup.R"))

## ---- Signal-detection theory: d' and criterion ------------------------------
# Build a yes/no detection table from a synthetic signal/noise design.
set.seed(20260621)
n_signal <- 200; n_noise <- 200
hits <- rbinom(1, n_signal, 0.80); fas <- rbinom(1, n_noise, 0.20)

sdt <- function(hits, n_signal, fas, n_noise) {
  # log-linear (Hautus, 1995) correction avoids infinite z at ceiling/floor
  H <- (hits + 0.5) / (n_signal + 1)
  F <- (fas  + 0.5) / (n_noise  + 1)
  dprime <- qnorm(H) - qnorm(F)
  crit   <- -0.5 * (qnorm(H) + qnorm(F))
  beta   <- exp(dprime * crit)
  c(dprime = dprime, criterion = crit, log_beta = log(beta),
    hit_rate = H, fa_rate = F)
}
cat("== signal-detection theory ==\n")
print(round(sdt(hits, n_signal, fas, n_noise), 3))

## ---- EZ-diffusion (Wagenmakers, van der Maas & Grasman, 2007) ---------------
# Recover drift rate (v), boundary separation (a), and non-decision time (Ter)
# from accuracy + the mean and variance of CORRECT RTs (in seconds).
ez_diffusion <- function(pc, vrt, mrt, s = 0.1) {
  if (pc == 1) pc <- 1 - .Machine$double.eps        # guard perfect accuracy
  if (pc == 0.5) pc <- 0.5 + 1e-6
  L <- qlogis(pc)
  x <- L * (L * pc^2 - L * pc + pc - 0.5) / vrt
  v <- sign(pc - 0.5) * s * x^(1 / 4)
  a <- s^2 * qlogis(pc) / v
  y <- -v * a / s^2
  mdt <- (a / (2 * v)) * (1 - exp(y)) / (1 + exp(y))  # mean decision time
  Ter <- mrt - mdt
  c(drift = v, boundary = a, non_decision = Ter)
}

# Per-condition EZ recovery from this kit's synthetic trials (RT -> seconds).
for (cd in levels(dat$cond)) {
  sub <- dat[dat$cond == cd, ]
  correct <- sub[sub$acc == 1, ]
  pc  <- mean(sub$acc)
  rts <- correct$rt / 1000
  est <- ez_diffusion(pc, var(rts), mean(rts))
  cat(sprintf("\n%-12s pc=%.3f  drift=%.3f boundary=%.3f Ter=%.3f s\n",
              cd, pc, est["drift"], est["boundary"], est["non_decision"]))
}

cat("\nInterpretation: a congruency cost localized to DRIFT (evidence quality)",
    "tells a different\nprocess story than one localized to BOUNDARY (caution)",
    "or Ter (encoding/motor).\n")
