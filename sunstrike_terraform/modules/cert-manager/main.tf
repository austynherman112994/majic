
resource "helm_release" "cert_manager" {

  namespace       = var.sunstrike_namespace
  name            = "cert-manager"
  timeout         = 600
  upgrade_install = true
  wait            = false

  repository = "https://charts.jetstack.io"
  chart      = "cert-manager"
  values     = [file("../../helm/cert-manager/local.yaml")]
}
