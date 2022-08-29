//declaring the packages

package test

//we are using serveral libraries here for testing
import (
	"testing"

	"github.com/gruntwork-io/terratest/modules/terraform"
	"github.com/stretchr/testify/assert"
)

//writing function to perform the test

func TestVpcNameCreate(t *testing.T) {
	t.Parallel()

	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{

		TerraformDir: "..//modules",

		Vars: map[string]interface{}{
			"region":   "us-east-1",
			"vpc_name": "test-vpc",
		},
	})
	//Run a Terraform init and apply from terraform options
	terraform.InitAndApply(t, terraformOptions)

	//Run a Terraform destroy at the end of the test
	defer terraform.Destroy(t, terraformOptions)

	// Run `terraform output` to get the values of output variables and check they have the expected values.
	output := terraform.Output(t, terraformOptions, "aws_vpc")
	assert.Equal(t, "aws_vpc", output)
}
