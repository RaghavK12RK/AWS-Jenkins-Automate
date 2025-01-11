resource "aws_vpc" "test_vpc" {
  cidr_block = var.cidr_block

   tags = {
    Name = "test-vpc-dev"
  }
}

resource "aws_subnet" "subnet-1" {
  vpc_id = aws_vpc.test_vpc.id
  cidr_block = var.subnet_cidr

  tags = {
    Name = "test-subnet-new"
  }
}

resource "aws_security_group" "vpc_subnet" {
    name = "vpc-SG"
    vpc_id = aws_vpc.test_vpc.id

    tags = {
        Name = "test"
    }
}

resource "aws_vpc_security_group_ingress_rule" "test_ingress_rule" {
  security_group_id = aws_security_group.vpc_subnet.id
  cidr_ipv4         = aws_vpc.test_vpc.cidr_block
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.test_vpc.id

  tags = {
    Name = "test-IGW"
  }
}
