variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "aws_profile" {
  type    = string
  default = ""
}

variable "aws_access_key" {
  type    = string
  default = ""
}

variable "aws_secret_key" {
  type    = string
  default = ""
}

variable "skip_credentials_validation" {
  type    = bool
  default = false
}

variable "skip_metadata_api_check" {
  type    = bool
  default = false
}

variable "skip_requesting_account_id" {
  type    = bool
  default = false
}

variable "skip_region_validation" {
  type    = bool
  default = false
}

variable "s3_use_path_style" {
  type    = bool
  default = false
}
