provider "aws" {
region = var.region
access_key = var.access_key
secret_key = var.secret_key
}

terraform {
  required_version = ">= 0.12"
}

resource "aws_vpc" "vpc_name" {
cidr_block = "10.0.0.0/16" # cidr block iteration found in the terraform.tfvars file
tags = {
Name = "vpc-test"
}
}

