//declaring the packages

package test

//we are using serveral libraries here for testing
import (
	"testing"
	"github.com/gruntwork-io/terratest/modules/terraform"
)

//writing function to perform the test

func TestTerraformVpcExample(t *testing.T){

	terraformOptions := terraform.WithDefault.RetryableErrors(t, &terraform.Options{

	Terraform.Dir: "../modules	",
	
	Vars: map[string]interface{}{
		"region"   = "us-east-1",
		"vpc_name" = "test-vpc",
	},
})
   //Run a Terraform init and apply from terraform options
   terraform.InitAndApply(t, terraformOptions)
   
   //Run a Terraform destroy at the end of the test
   defer terraform.Destroy(t, terraformOptions)

   vpcArn := terraform.Output(t, terraform options, "")
   vpcId := terraform.Output(t, terraform options, "")

}
