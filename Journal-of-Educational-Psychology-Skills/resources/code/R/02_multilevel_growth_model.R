# Multilevel and growth-model templates for Journal of Educational Psychology.

if (!exists("student_data") || !exists("long_growth")) source("R/00_setup.R")

message_section("Multilevel outcome model")

student_data$z_prior <- standardize(student_data$prior_score)
student_data$z_post <- standardize(student_data$post_score)

if (pkg_available("lme4")) {
  model_outcome <- lme4::lmer(
    z_post ~ treat + z_prior + (1 | school_id/class_id),
    data = student_data,
    REML = FALSE
  )
  print(summary(model_outcome))
  ci <- stats::confint(model_outcome, parm = "treat", method = "Wald")
  cat("\nTreatment coefficient with 95% CI:\n")
  print(ci)
} else {
  model_outcome <- stats::lm(z_post ~ treat + z_prior + factor(class_id), data = student_data)
  print(summary(model_outcome))
  cat("\nFallback model uses classroom fixed effects. Install lme4 for random-effects nesting.\n")
}

message_section("Growth model")

long_growth$z_reading <- standardize(long_growth$reading_score)
long_growth$month_c <- long_growth$month - min(long_growth$month)

if (pkg_available("lme4")) {
  model_growth <- lme4::lmer(
    z_reading ~ month_c * treat + (1 + month_c | student_id) + (1 | class_id),
    data = long_growth,
    REML = FALSE
  )
  print(summary(model_growth))
  cat("\nJEP interpretation target: report the month x treatment coefficient as a change in learning\n")
  cat("slope, with CI, and translate it into an educationally meaningful effect size.\n")
} else {
  model_growth <- stats::lm(z_reading ~ month_c * treat + factor(student_id) + factor(class_id), data = long_growth)
  print(summary(model_growth))
  cat("\nFallback model uses fixed effects for students/classes. Install lme4 for growth random effects.\n")
}

effect_d <- cohens_d(student_data$post_score, student_data$treat)
cat("\nRaw post-score Cohen's d (unadjusted teaching example):", round(effect_d, 3), "\n")
cat("Do not report this alone in a manuscript; pair it with the preregistered adjusted model.\n")
