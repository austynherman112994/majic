variable "env" {
  type        = string
  description = "Environment to deploy sunstrike into."
  default     = "local"
}


variable "sunstrike_namespace" {
  type        = string
  description = "Namespace to deploy sunstrike into."
  default     = "sunstrike"
}
