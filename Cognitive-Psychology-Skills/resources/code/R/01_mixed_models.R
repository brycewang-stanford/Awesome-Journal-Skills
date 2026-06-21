# 01_mixed_models.R — (G)LMM over crossed subject & item random effects
# The workhorse Cognitive Psychology analysis: do NOT aggregate to subject means.
# Source 00_setup.R first.

if (!exists("dat")) source(file.path("R", "00_setup.R"))

if (!requireNamespace("lme4", quietly = TRUE)) {
  message("lme4 not installed; showing the by-subject fallback only.")
} else {
  suppressPackageStartupMessages(library(lme4))

  ## ---- log-RT linear mixed model, MAXIMAL random-effects structure ----------
  # Random intercepts + congruency slopes for subjects; random intercepts for items.
  # If a maximal model fails to converge, simplify principledly (drop correlations,
  # then the least-supported slope) — never silently default to random intercepts.
  m_rt <- lmer(log_rt ~ c_cond + (1 + c_cond | subj) + (1 | item),
               data = dat, REML = TRUE,
               control = lmerControl(optimizer = "bobyqa"))
  cat("\n== log-RT LMM ==\n"); print(summary(m_rt)$coefficients)

  if (requireNamespace("lmerTest", quietly = TRUE)) {
    m_rt_t <- lmerTest::lmer(log_rt ~ c_cond + (1 + c_cond | subj) + (1 | item),
                             data = dat,
                             control = lmerControl(optimizer = "bobyqa"))
    cat("\n-- Satterthwaite p-values --\n")
    print(summary(m_rt_t)$coefficients)
  }

  ## ---- accuracy GLMM (binomial) ---------------------------------------------
  m_acc <- glmer(acc ~ c_cond + (1 | subj) + (1 | item),
                 data = dat, family = binomial,
                 control = glmerControl(optimizer = "bobyqa"))
  cat("\n== accuracy GLMM (logit) ==\n"); print(summary(m_acc)$coefficients)

  ## ---- model-implied condition means + contrast -----------------------------
  if (requireNamespace("emmeans", quietly = TRUE)) {
    em <- emmeans::emmeans(m_rt, ~ c_cond, at = list(c_cond = c(-0.5, 0.5)))
    cat("\n== estimated marginal means (log-RT) ==\n"); print(em)
    cat("\n== congruency contrast ==\n"); print(pairs(em))
  }
}

## ---- effect size with uncertainty (always reported alongside p) -------------
agg <- aggregate(rt ~ subj + cond, data = dat, FUN = mean)
wide <- reshape(agg, idvar = "subj", timevar = "cond", direction = "wide")
dz <- cohen_dz(wide$`rt.incongruent`, wide$`rt.congruent`)
cat(sprintf("\nWithin-subject Cohen's d_z (RT cost) = %.3f\n", dz))
if (requireNamespace("effectsize", quietly = TRUE)) {
  print(effectsize::cohens_d(wide$`rt.incongruent`, wide$`rt.congruent`, paired = TRUE))
}
