# Synthetic setup for Journal of Educational Psychology analysis templates.
# Run from Journal-of-Educational-Psychology-Skills/resources/code.

set.seed(20260621)

message_section <- function(title) {
  cat("\n", paste(rep("=", nchar(title)), collapse = ""), "\n", sep = "")
  cat(title, "\n", sep = "")
  cat(paste(rep("=", nchar(title)), collapse = ""), "\n", sep = "")
}

pkg_available <- function(pkg) {
  requireNamespace(pkg, quietly = TRUE)
}

standardize <- function(x) {
  as.numeric(scale(x))
}

ci_mean <- function(x, level = 0.95) {
  x <- x[is.finite(x)]
  se <- stats::sd(x) / sqrt(length(x))
  crit <- stats::qt((1 + level) / 2, df = length(x) - 1)
  c(mean = mean(x), lower = mean(x) - crit * se, upper = mean(x) + crit * se)
}

cohens_d <- function(y, group) {
  group <- as.factor(group)
  if (nlevels(group) != 2) stop("cohens_d expects exactly two groups")
  y0 <- y[group == levels(group)[1]]
  y1 <- y[group == levels(group)[2]]
  pooled <- sqrt(((length(y0) - 1) * stats::var(y0) + (length(y1) - 1) * stats::var(y1)) /
    (length(y0) + length(y1) - 2))
  (mean(y1) - mean(y0)) / pooled
}

n_schools <- 12
classes_per_school <- sample(3:5, n_schools, replace = TRUE)
class_lookup <- data.frame(
  school_id = rep(seq_len(n_schools), classes_per_school),
  class_id = seq_len(sum(classes_per_school))
)
class_lookup$treat <- as.integer(ave(
  class_lookup$class_id,
  class_lookup$school_id,
  FUN = function(z) sample(rep(c(0, 1), length.out = length(z)))
))
class_lookup$class_quality <- rnorm(nrow(class_lookup), 0, 0.35)

rows <- lapply(seq_len(nrow(class_lookup)), function(i) {
  n_students <- sample(18:30, 1)
  data.frame(
    school_id = class_lookup$school_id[i],
    class_id = class_lookup$class_id[i],
    treat = class_lookup$treat[i],
    class_quality = class_lookup$class_quality[i],
    student_id = seq_len(n_students)
  )
})

student_data <- do.call(rbind, rows)
student_data$student_id <- seq_len(nrow(student_data))
school_effect <- rnorm(n_schools, 0, 0.25)
class_effect <- rnorm(max(student_data$class_id), 0, 0.30)

student_data$prior_score <- 0.45 * school_effect[student_data$school_id] +
  0.35 * class_effect[student_data$class_id] + rnorm(nrow(student_data), 0, 1)
student_data$motivation <- 0.30 * student_data$treat +
  0.35 * standardize(student_data$prior_score) +
  0.20 * student_data$class_quality +
  rnorm(nrow(student_data), 0, 0.80)
student_data$post_score <- 0.35 * student_data$treat +
  0.45 * standardize(student_data$motivation) +
  0.50 * standardize(student_data$prior_score) +
  school_effect[student_data$school_id] +
  class_effect[student_data$class_id] +
  rnorm(nrow(student_data), 0, 0.85)

long_growth <- do.call(rbind, lapply(0:3, function(month) {
  out <- student_data[, c("school_id", "class_id", "student_id", "treat", "prior_score")]
  out$month <- month
  out$reading_score <- 0.55 * standardize(out$prior_score) +
    0.18 * month +
    0.12 * out$treat * month +
    class_effect[out$class_id] +
    rnorm(nrow(out), 0, 0.70)
  out
}))

jars_disclosure <- list(
  design = "cluster-randomized classroom intervention with students nested in classes/schools",
  sample_units = c("student", "classroom", "school"),
  confirmatory = c("treatment effect on post_score controlling for prior_score", "motivation mediation"),
  exploratory = c("school-level heterogeneity in treatment slope"),
  transparency = "synthetic example; replace with repository DOI, preregistration URL, and JARS checklist"
)

message_section("Synthetic JEP data ready")
cat("Students:", nrow(student_data), "\n")
cat("Classes:", length(unique(student_data$class_id)), "\n")
cat("Schools:", length(unique(student_data$school_id)), "\n")
