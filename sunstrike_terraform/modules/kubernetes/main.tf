

resource "kubernetes_namespace" "sunstrike_namespace" {
  metadata {
    name = var.sunstrike_namespace
  }

}
