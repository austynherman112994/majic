
resource "helm_release" "loki" {

  namespace       = var.sunstrike_namespace
  name            = "loki"
  timeout         = 600
  upgrade_install = true
  wait            = false

  repository = "https://grafana.github.io/helm-charts"
  chart      = "loki"
  values     = [file("../../helm/loki/local.yaml")]
}
