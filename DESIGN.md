# Design Document – Cost Optimization Janitor

## 1. System Overview

This project implements a cost optimization tool that identifies unused AWS resources and estimates potential cost savings. The system is built using Python and interacts with AWS services through the boto3 SDK. 

For safe development and testing, LocalStack is used to simulate AWS services locally. The solution is integrated with a CI/CD pipeline using GitHub Actions.

---

## 2. Architecture Design

The system follows a simple automated workflow:

1. Code is pushed to the repository
2. GitHub Actions pipeline is triggered
3. LocalStack container is started
4. The janitor script is executed
5. The script connects to simulated AWS services using boto3
6. It fetches EC2 volumes and S3 buckets
7. Unused resources are identified
8. Estimated cost is calculated
9. Results are output in JSON format

This design ensures automation, repeatability, and safe testing without using real cloud resources.

---

## 3. Multi-Cloud Design

The current implementation is AWS-specific, but the system can be extended to support multiple cloud providers.

A modular design can be introduced where each cloud provider has its own implementation:

- AWS → boto3
- Azure → Azure SDK
- GCP → Google Cloud SDK

A common interface can standardize resource detection and cost calculation across providers. This allows the system to be extended without major changes to the core logic.

---

## 4. IAM and Security

In a real AWS environment, the system would use IAM roles with the principle of least privilege.

Required permissions include:
- ec2:DescribeVolumes
- ec2:DeleteVolume
- s3:ListBucket

Sensitive information such as access keys should not be hardcoded. Instead, environment variables or secret management services should be used.

---

## 5. Failure Scenarios

The system may encounter the following failures:

1. LocalStack not ready when the script runs, causing connection errors
2. API failures from boto3 due to service unavailability
3. Missing or invalid credentials in a real AWS environment
4. Network-related issues preventing access to services

These can be handled using retries, health checks, and proper error handling.

---

## 6. Monitoring and Metrics

In a production setup, the following metrics would be useful:

- Number of unused resources detected
- Estimated monthly cost savings
- Script execution success or failure rate

Logs can be integrated with monitoring tools such as AWS CloudWatch for better observability.

---

## 7. Design Decisions and Trade-offs

- LocalStack was used instead of real AWS to avoid cost and enable safe testing
- Static pricing was used for cost calculation instead of real-time pricing APIs to simplify implementation
- The focus was on EBS volumes as a primary cost factor for demonstration
- A simple architecture was chosen to keep the system easy to understand and extend

---

## 8. Conclusion

This system demonstrates a basic but practical approach to cloud cost optimization.
