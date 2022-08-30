terraform {
  source = "git::git@github.com:RaghavK12RK/AWS-Jenkins-Automate.git//modules?ref=main"
}

locals {

datadog_api_key = "6e3f3f173d4c41b35272d56821468f59"
datadog_app_key = "def70b458195df80201f0ae312afe41cc48e8e5b"
user_email_id   = "raoraghavendra502@gmail.com"
BU-L2_shortname = "Sre"
BU-L3_shortname = "Ops"
dd_role         = "Datadog Admin Role"

}

inputs = {
datadog_api_key = local.datadog_api_key
datadog_app_key = local.datadog_app_key
user_email_id   = local.user_email_id
BU-L2_shortname = local.BU-L2_shortname
BU-L3_shortname = local.BU-L3_shortname
dd_role         = local.dd_role

}
