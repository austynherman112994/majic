
resource "null_resource" "pulsar_init" {
  provisioner "local-exec" {
    command = "bash ../../scripts/pulsar/prepare_helm_release.sh -n sunstrike -k pulsar"
  }
}

resource "helm_release" "pulsar" {
  depends_on = ["null_resource.pulsar_init"]

  namespace       = "sunstrike"
  name            = "pulsar"
  timeout         = 600
  upgrade_install = true
  wait            = false

  repository = "https://pulsar.apache.org/charts"
  chart      = "pulsar"
  values     = [file("../../helm/pulsar/local.yaml")]
}
