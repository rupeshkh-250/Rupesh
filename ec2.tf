provider "aws" {
    region = "us-east-1" # specify the AWS region where you want to create the EC2 instance
}
resource "aws_instance" "this" {
  ami                     = "ami-0ec10929233384c7f" # AMI ID for ubuntu 20.04 in us-east-1 region, you can change it based on your needs and region
  instance_type           = "t2.micro"
 
}