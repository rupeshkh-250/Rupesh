# Submission – Cost Optimization Janitor

## Candidate Information
Name: Moses A

---

## Project Summary

This project implements a cost optimization tool that identifies unused AWS resources and estimates potential monthly cost savings.

The solution is built using Python (boto3) and tested using LocalStack to simulate AWS services. It also includes a CI/CD pipeline using GitHub Actions for automated execution.

---

## Features Implemented

- Detection of unused EBS volumes
- Listing of S3 buckets
- Monthly cost estimation based on volume size
- Dry run mode for safe execution
- Delete mode to clean unused resources
- CI/CD pipeline for automated execution

---

## How to Run Locally

### 1. Start LocalStack

```bash
docker run -d -p 4566:4566 -e SERVICES=s3,ec2 localstack/localstack
```

### 2. Install Dependencies

```bash
pip install boto3
```

### 3. Run Script (Dry Run)

```bash
python janitor/janitor.py
```

### 4. Run Script (Delete Mode)

```bash
python janitor/janitor.py --delete
```

---

## CI/CD Pipeline

The GitHub Actions workflow performs the following steps:

1. Sets up the Python environment
2. Installs dependencies
3. Starts LocalStack using Docker
4. Waits until LocalStack is ready
5. Executes the janitor script (dry run)
6. Executes delete mode

Workflow file:
```
.github/workflows/cost-janitor.yml
```

---

## Sample Output

```json
{
  "unused_volumes": [
    {
      "VolumeId": "vol-123",
      "Size": 8,
      "State": "available"
    }
  ],
  "monthly_waste_cost": 0.64,
  "buckets": ["my-log-bucket"]
}
```

---

## Assumptions

- EBS pricing is assumed as $0.08 per GB per month
- LocalStack is used instead of real AWS to avoid cost
- Only EBS volumes are considered for cost calculation

---

## Limitations

- Uses static pricing instead of real AWS pricing API
- Limited to basic AWS resources (EC2 and S3)
- Does not include advanced tagging or filtering logic

---

## Notes

- The project is designed for demonstration and learning purposes
- The same logic can be extended to real AWS with proper credentials and IAM setup

---
