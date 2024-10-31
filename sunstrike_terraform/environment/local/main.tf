

module "minikube" {
  source = "../../modules/minikube"
  env    = var.env
}

module "kubernetes" {
  source = "../../modules/kubernetes"
  env    = var.env
}

module "helm" {
  source = "../../modules/helm"
  env    = var.env
}

module "pulsar" {
  source     = "../../modules/pulsar"
  env        = var.env
  depends_on = [module.kubernetes, module.helm]
}

module "grafana" {
  source     = "../../modules/grafana"
  env        = var.env
  depends_on = [module.kubernetes, module.helm]
}

module "loki" {
  source     = "../../modules/loki"
  env        = var.env
  depends_on = [module.kubernetes, module.helm]
}

module "cert-manager" {
  source     = "../../modules/cert-manager"
  env        = var.env
  depends_on = [module.kubernetes, module.helm]
}


module "otel" {
  source     = "../../modules/otel"
  env        = var.env
  depends_on = [module.kubernetes, module.helm, module.cert-manager]
}

module "redis" {
  source     = "../../modules/redis"
  env        = var.env
  depends_on = [module.kubernetes, module.helm, module.cert-manager]
}
