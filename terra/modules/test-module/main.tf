terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.83"
    }
  }
}

provider "aws" {
    access_key = ""
    secret_key = ""
    region = var.region_name
}


module "vpc" {
    source = "../vpc-ec2"
      
    region_name = var.region_name
    cidr_block = var.cidr_block
    subnet_cidr = var.subnet_cidr
}