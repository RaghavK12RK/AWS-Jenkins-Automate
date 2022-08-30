# ---------------------------------------------------------------------------------------------------------------------
# REQUIRED MODULE PARAMETERS
# These variables must be passed in by the operator.
# ---------------------------------------------------------------------------------------------------------------------

variable "datadog_api_key" {
    description = "the api key is unique for our organisation"
}

variable "datadog_app_key" {
    description = "the application key is unique for our organisation"
}

variable "tmna_email_id" {
    description = "user email id for invite"
}

variable "BU-L2_shortname" {
    description = "Name of the L2 suborganization"
}

variable "BU-L3_shortname" {
    description = "Name of the L3 suborganization"
}

variable "dd_role" {
    description = "Filter to determine Admin access"
    type        = string
}
