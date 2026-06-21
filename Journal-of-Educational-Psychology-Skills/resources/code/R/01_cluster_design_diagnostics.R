# Cluster-design diagnostics for Journal of Educational Psychology manuscripts.

if (!exists("student_data")) source("R/00_setup.R")

message_section("Cluster design diagnostics")

icc_oneway <- function(y, cluster) {
  df <- data.frame(y = y, cluster = as.factor(cluster))
  fit <- stats::aov(y ~ cluster, data = df)
  tab <- summary(fit)[[1]]
  ms_between <- tab[["Mean Sq"]][1]
  ms_within <- tab[["Mean Sq"]][2]
  k_bar <- mean(table(df$cluster))
  (ms_between - ms_within) / (ms_between + (k_bar - 1) * ms_within)
}

cluster_sizes <- as.data.frame(table(student_data$class_id))
names(cluster_sizes) <- c("class_id", "n_students")
cluster_sizes$class_id <- as.integer(as.character(cluster_sizes$class_id))
cluster_sizes <- merge(cluster_sizes, unique(student_data[, c("class_id", "school_id", "treat")]), by = "class_id")

icc_prior <- icc_oneway(student_data$prior_score, student_data$class_id)
icc_post <- icc_oneway(student_data$post_score, student_data$class_id)
imbalance_ratio <- max(cluster_sizes$n_students) / min(cluster_sizes$n_students)
balance_table <- aggregate(n_students ~ treat, data = cluster_sizes, FUN = function(x) {
  paste0(length(x), " classes / mean n=", round(mean(x), 1))
})

design_effect <- 1 + (mean(cluster_sizes$n_students) - 1) * max(icc_post, 0)
effective_n <- nrow(student_data) / design_effect
mde_sketch <- 2.80 / sqrt(effective_n) # rough two-arm sketch, not a substitute for power simulation

diagnostics <- data.frame(
  diagnostic = c("ICC prior", "ICC post", "cluster-size imbalance", "design effect", "effective N sketch", "MDE sketch"),
  value = round(c(icc_prior, icc_post, imbalance_ratio, design_effect, effective_n, mde_sketch), 3)
)

print(diagnostics, row.names = FALSE)
print(balance_table, row.names = FALSE)

if (pkg_available("lme4")) {
  fit_null <- lme4::lmer(post_score ~ 1 + (1 | class_id), data = student_data, REML = TRUE)
  cat("\nlme4 null model variance components:\n")
  print(lme4::VarCorr(fit_null), comp = "Variance")
} else {
  cat("\nInstall lme4 for mixed-model variance components; base-R ICC shown above.\n")
}

cat("\nJEP reporting note: state the randomization unit, analysis unit, ICC, cluster sizes, and whether\n")
cat("the power analysis used the same nesting structure as the confirmatory model.\n")
