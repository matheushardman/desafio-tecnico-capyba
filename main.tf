terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.57.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = "us-east-1" #Norte da Virginia
}
resource "random_id" "key_suffix" {
  byte_length = 4
}

resource "aws_key_pair" "user_ec2_key" {
  key_name   = "user_ec2_${random_id.key_suffix.hex}"
  public_key = file("~/.ssh/id_rsa.pub")
}