variable "region_name" {
    type = string 
    default = "ap-south-1"
}

variable "cidr_block" {
  type = string
  default = "10.0.0.0/16"
}

variable "subnet_cidr" {
  type = string
  default = "10.0.0.0/22"
}