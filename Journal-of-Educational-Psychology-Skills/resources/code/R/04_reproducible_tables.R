# Reproducible APA/JEP table skeletons.

if (!exists("student_data")) source("R/00_setup.R")

message_section("Table 1: descriptives by condition")

table1 <- aggregate(
  cbind(prior_score, motivation, post_score) ~ treat,
  data = student_data,
  FUN = function(x) sprintf("%.2f (%.2f)", mean(x), stats::sd(x))
)
table1$treat <- ifelse(table1$treat == 1, "Intervention", "Control")
print(table1, row.names = FALSE)

message_section("Table 2: model-summary skeleton")

student_data$z_prior <- standardize(student_data$prior_score)
student_data$z_post <- standardize(student_data$post_score)
fit <- stats::lm(z_post ~ treat + z_prior, data = student_data)
coef_tab <- summary(fit)$coefficients
ci_tab <- stats::confint(fit)
table2 <- data.frame(
  term = rownames(coef_tab),
  estimate = round(coef_tab[, "Estimate"], 3),
  se = round(coef_tab[, "Std. Error"], 3),
  ci_lower = round(ci_tab[, 1], 3),
  ci_upper = round(ci_tab[, 2], 3),
  p = signif(coef_tab[, "Pr(>|t|)"], 3),
  row.names = NULL
)
print(table2, row.names = FALSE)

message_section("Transparency and Openness note")

transparency_note <- data.frame(
  item = c("Data", "Materials", "Analysis code", "Preregistration", "Reporting standard"),
  manuscript_text = c(
    "Repository DOI or protected-access explanation goes here.",
    "Intervention materials and measures repository DOI goes here.",
    "R scripts and session info deposited with the manuscript package.",
    "URL and deviations, or explicit 'not preregistered' statement.",
    "JARS/JARS-REC checklist completed for the design."
  )
)
print(transparency_note, row.names = FALSE)

cat("\nJEP table note: include N at every analytic level, effect sizes with CIs, and enough\n")
cat("model information for reviewers to match tables to the preregistered analysis plan.\n")
