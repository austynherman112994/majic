variable "env" {
  type        = string
  description = "Environment to deploy sunstrike into."
  default     = "local"
}

variable "config_path" {
  type        = string
  description = "Path to the kube config."
  default     = "~/.kube/config"
}


variable "config_context" {
  type        = string
  description = "Kube context to use."
  default     = "minikube"
}

variable "sunstrike_namespace" {
  type        = string
  description = "Namespace to deploy sunstrike into."
  default     = "sunstrike"
}

