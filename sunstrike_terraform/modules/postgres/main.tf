
resource "helm_release" "postgresql" {

  namespace       = var.sunstrike_namespace
  name            = "postgresql"
  timeout         = 600
  upgrade_install = true
  wait            = false

  repository = "oci://registry-1.docker.io/bitnamicharts/"
  chart      = "postgresql"
  values     = [file("../../helm/postgresql/local.yaml")]
}
