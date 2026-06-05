# Cost Optimization Janitor (AWS + LocalStack)

[![CI](https://github.com/rupeshkh-250/Rupesh/actions/workflows/ci.yml/badge.svg)](https://github.com/rupeshkh-250/Rupesh/actions)

## Project Overview
This project is a cost optimization tool built using Python and AWS services (simulated using LocalStack). It identifies unused resources and estimates potential cost savings.

The tool focuses on:
- Unused EBS volumes
- S3 buckets
- Monthly cost estimation

It also provides an option to delete unused resources.

---

## Features

- Detect unused EC2 volumes
- List S3 buckets
- Calculate monthly cost waste
- Dry run mode for safe execution
- Delete mode for cleanup
- CI/CD pipeline using GitHub Actions
- Local testing using LocalStack

---

## Tech Stack

- Python (Boto3)
- AWS (EC2, S3)
- LocalStack
- Docker
- GitHub Actions
- Terraform

---

## Project Structure

```
devops-assignment/
│
├── janitor/
│   └── janitor.py
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── .github/workflows/
│   └── cost-janitor.yml
│
├── requirements.txt
└── README.md
```

---

## How It Works

1. Connects to AWS services using LocalStack endpoint
2. Fetches EC2 volumes and filters unused volumes (state = available)
3. Calculates monthly cost based on volume size
4. Lists available S3 buckets
5. Outputs results in JSON format

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

## Running Locally

### Start LocalStack

```bash
docker run -d -p 4566:4566 -e SERVICES=s3,ec2 localstack/localstack
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run (Dry Run Mode)

```bash
python janitor/janitor.py
```

### Run (Delete Mode)

```bash
python janitor/janitor.py --delete
```

---

## CI/CD Pipeline

The GitHub Actions workflow performs the following:

1. Sets up Python environment
2. Installs dependencies
3. Starts LocalStack container
4. Waits for service readiness
5. Runs janitor script (dry run)
6. Runs delete mode

Workflow file:
```
.github/workflows/cost-janitor.yml
```

---

## Important Notes

- LocalStack is used to simulate AWS services
- No real AWS resources are used
- Dry run mode is default for safety
- Delete mode should be used cautiously

---

## Key Learnings

- AWS automation using Boto3
- LocalStack-based testing
- CI/CD implementation with GitHub Actions
- Debugging container-based workflows
- Cost optimization strategies

---

## Author

Moses A
