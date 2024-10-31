
resource "helm_release" "grafana" {

  namespace       = var.sunstrike_namespace
  name            = "grafana"
  timeout         = 600
  upgrade_install = true
  wait            = false

  repository = "https://grafana.github.io/helm-charts"
  chart      = "grafana"
  values     = [file("../../helm/grafana/local.yaml")]
}
