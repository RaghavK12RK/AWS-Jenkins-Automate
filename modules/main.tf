# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CREATE AN DD ORGANIZATION WITH USER AND ROLE ATTACHMENT MODULE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----------------------------------------------------------------------------------------------------------------------
# REQUIRE A SPECIFIC TERRAFORM VERSION OR HIGHER
# This module has been updated with 0.12 syntax, which means it is no longer compatible with any versions below 0.12.
# ----------------------------------------------------------------------------------------------------------------------

terraform {
  # Only allow this Terraform version. Note that if you upgrade to a newer version, Terraform won't allow you to use an
  # older version, so when you upgrade, you should upgrade everyone on your team and your CI servers all at once.
  required_version = ">= 0.13"

  required_providers {
   datadog = {
      source = "DataDog/datadog"
      version = ">=3.0.0"
    }
  }
}

# Configure the Datadog provider
provider "datadog" {
  api_key = var.datadog_api_key
  app_key = var.datadog_app_key
}

# ----------------------------------------------------------------------------------------------------------------------
# RESOURCE SECTION
# ----------------------------------------------------------------------------------------------------------------------

# Create a new Datadog Child Organization
resource "datadog_child_organization" "New_organization_name" {
  name = "${var.BU-L2_shortname}-${var.BU-L3_shortname}"
}

# Creating an Datadog user with the role attachment
data "datadog_role" "permission" {
  filter = var.dd_role
}

# Create a new Datadog user
resource "datadog_user" "user_email" {
  email = var.user_email_id
  roles = [data.datadog_role.permission.id]
}



