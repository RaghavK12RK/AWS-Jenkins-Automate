output "user_email" {
  value  = var.tmna_email_id
}

output "organisation_name" {
  value  = datadog_child_organization.New_organization_name.name
}
