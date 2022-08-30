package test

import (
	"testing"

	"github.com/gruntwork-io/terratest/modules/logger"
	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/stretchr/testify/assert"
)

func TestDatadogUserCreate(t *testing.T) {
	t.Parallel()

	expectedDatadogUserName := "raghu.rk114@gmail.com"

	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
		// Set the path to the Terraform code that will be tested.
		TerraformDir:    "../modules",
		TerraformBinary: "terragrunt",
		Vars:            map[string]interface{}{},
	})
	// Clean up resources with "terraform destroy" at the end of the test.
	defer terraform.Destroy(t, terraformOptions)

	// Run "terraform init" and "terraform apply". Fail the test if there are any errors.
	terraform.InitAndApply(t, terraformOptions)

	// Run `terraform output` to get the values of output variables and check they have the expected values.
	datadog_user := terraform.Output(t, terraformOptions, "datadog_user")

	// Verify we're getting back the outputs we expect
	assert.Equal(t, expectedDatadogUserName, datadog_user)

	// Console logs
	logger.Logf(t, "datadogUserName is %s", datadog_user)
}
