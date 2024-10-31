
resource "helm_release" "otel_operator" {

  namespace       = var.sunstrike_namespace
  name            = "otel-operator"
  timeout         = 600
  upgrade_install = true
  wait            = false

  repository = "https://open-telemetry.github.io/opentelemetry-helm-charts"
  chart      = "opentelemetry-operator"
  values     = [file("../../helm/otel/operator/local.yaml")]
}

resource "helm_release" "otel_collector" {
  depends_on      = [helm_release.otel_operator]
  namespace       = var.sunstrike_namespace
  name            = "otel-collector"
  timeout         = 600
  upgrade_install = true
  wait            = false

  repository = "https://open-telemetry.github.io/opentelemetry-helm-charts"
  chart      = "opentelemetry-collector"
  values     = [file("../../helm/otel/collector/local.yaml")]
}
