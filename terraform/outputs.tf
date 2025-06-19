output "kube_config" {
  value = module.aks.kube_config
}
output "kube_config" {
  value = module.aks.kube_config
}

output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}

output "log_analytics_workspace_id" {
  value = azurerm_log_analytics_workspace.log.id
}
