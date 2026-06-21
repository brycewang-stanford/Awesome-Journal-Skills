# Mediation and JARS-style disclosure template for Journal of Educational Psychology.

if (!exists("student_data") || !exists("jars_disclosure")) source("R/00_setup.R")

message_section("Learning-mechanism mediation")

student_data$z_prior <- standardize(student_data$prior_score)
student_data$z_motivation <- standardize(student_data$motivation)
student_data$z_post <- standardize(student_data$post_score)

if (pkg_available("lavaan")) {
  mediation_model <- "
    z_motivation ~ a*treat + z_prior
    z_post ~ b*z_motivation + cprime*treat + z_prior
    indirect := a*b
    total := cprime + (a*b)
  "
  fit <- lavaan::sem(mediation_model, data = student_data, se = "bootstrap", bootstrap = 1000)
  print(lavaan::summary(fit, standardized = TRUE, fit.measures = TRUE, ci = TRUE))
} else {
  model_a <- stats::lm(z_motivation ~ treat + z_prior, data = student_data)
  model_b <- stats::lm(z_post ~ z_motivation + treat + z_prior, data = student_data)
  a <- stats::coef(model_a)[["treat"]]
  b <- stats::coef(model_b)[["z_motivation"]]
  indirect <- a * b

  boot_indirect <- replicate(1000, {
    idx <- sample(seq_len(nrow(student_data)), replace = TRUE)
    d <- student_data[idx, ]
    a_b <- stats::coef(stats::lm(z_motivation ~ treat + z_prior, data = d))[["treat"]]
    b_b <- stats::coef(stats::lm(z_post ~ z_motivation + treat + z_prior, data = d))[["z_motivation"]]
    a_b * b_b
  })

  cat("Base-R indirect effect:", round(indirect, 3), "\n")
  cat("Bootstrap 95% CI:", paste(round(stats::quantile(boot_indirect, c(.025, .975)), 3), collapse = " to "), "\n")
  cat("Install lavaan for SEM fit indices, standardized paths, and a publication-grade mediation model.\n")
}

message_section("JARS disclosure skeleton")
print(jars_disclosure)

cat("\nManuscript checklist:\n")
cat("- Label mediation as confirmatory only if preregistered before data inspection.\n")
cat("- Report sample units at student, classroom, and school levels.\n")
cat("- State missing-data handling, reliability/validity evidence, and exact CI method.\n")
cat("- Deposit analysis code and synthetic/redacted reproduction material when protected data cannot be open.\n")
