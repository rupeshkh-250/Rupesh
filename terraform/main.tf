terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "= 4.67.0"
    }
  }
}


provider "aws" {
  region = var.aws_region

  # Optional credentials: if unset, Terraform will use the profile or environment
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  profile    = var.aws_profile

  skip_credentials_validation = var.skip_credentials_validation
  skip_metadata_api_check     = var.skip_metadata_api_check
  skip_requesting_account_id  = var.skip_requesting_account_id
  skip_region_validation      = var.skip_region_validation

  s3_use_path_style = var.s3_use_path_style
}
# ---------------------------
# VPC
# ---------------------------
resource "aws_vpc" "main" {
  cidr_block = "10.20.0.0/16"

  tags = {
    Name = "main-vpc"
  }
}

# ---------------------------
# Subnet
# ---------------------------
resource "aws_subnet" "public1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.20.1.0/24"
  availability_zone       = "us-east-1a"

  tags = {
    Name = "public-subnet"
  }
}

# ---------------------------
# S3 Bucket
# ---------------------------
resource "aws_s3_bucket" "logs" {
  bucket = "my-log-bucket"

  tags = {
    Name = "log-bucket"
  }
}

# ---------------------------
# EBS Volume (Orphan Example)
# ---------------------------
resource "aws_ebs_volume" "orphan" {
  availability_zone = "us-east-1a"
  size              = 8

  tags = {
    Project     = "NimbusKart"
    Environment = "staging"
    Owner       = "Moss"
    ManagedBy   = "terraform"
  }
}