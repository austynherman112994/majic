
resource "helm_release" "redis" {

  namespace       = var.sunstrike_namespace
  name            = "redis"
  timeout         = 600
  upgrade_install = true
  wait            = false

  repository = "oci://registry-1.docker.io/bitnamicharts/"
  chart      = "redis"
  values     = [file("../../helm/redis/local.yaml")]
}
