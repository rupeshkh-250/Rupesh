terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "= 4.67.0"
    }
  }
}


provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"

  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
  skip_region_validation      = true

  s3_use_path_style           = true   

  endpoints {
    s3  = "http://localhost:4566"
    ec2 = "http://localhost:4566"
    iam = "http://localhost:4566"
    sts = "http://localhost:4566"
  }
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