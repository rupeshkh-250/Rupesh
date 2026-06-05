# Cost Optimization Janitor (Local)

## Project Overview
This project is a lightweight cost-reporting tool that runs locally using a
sample report. The repository no longer depends on AWS or GitHub Actions.

The tool focuses on:
- Reading an existing cost/report JSON
- Calculating monthly EBS waste cost based on volume sizes
- Listing buckets found in the report

---

## Features

- Local-only operation (no AWS SDK required)
- Reads `samples/report.example.json` by default
- Calculates monthly waste cost

---

## Project Structure

```
aws-cost-janitor/
├── janitor/
│   └── janitor.py
├── janitor/requirements.txt
├── janitor/tests/
├── samples/
│   └── report.example.json
└── README.md
```

---

## Running Locally

### Install Dependencies

```bash
pip install -r janitor/requirements.txt
```

### Run (Local Dry Run)

```bash
python -m janitor.janitor --local
```

### Provide a custom report

```bash
python -m janitor.janitor --report samples/report.example.json
```

---

## Notes

- This repository no longer includes Terraform files or GitHub Actions workflows.
- Destructive operations (deleting real resources) are intentionally disabled.

---

## Author

Moses A
