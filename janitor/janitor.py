"""Janitor (local mode)

This simplified version removes the runtime dependency on AWS. By default it
loads a sample report from `samples/report.example.json` and calculates
monthly waste cost. For safety and to avoid requiring `boto3`, AWS calls are
not used.
"""

import argparse
import json
import os
from typing import List

try:
    from .constants import EBS_COST_PER_GB
except Exception:
    try:
        from constants import EBS_COST_PER_GB
    except Exception:
        EBS_COST_PER_GB = 0.08


def load_sample_report(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def calculate_cost(volumes: List[dict]) -> float:
    total = sum(v.get("Size", 0) * EBS_COST_PER_GB for v in volumes)
    return round(total, 2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="store_true", help="Use local sample report")
    parser.add_argument("--report", type=str, help="Path to JSON report to read")
    parser.add_argument("--delete", action="store_true", help="(noop) Delete unused volumes — not supported in local mode")
    args = parser.parse_args()

    print("Janitor started (local mode)...")

    # Prefer explicit report path, then bundled sample
    if args.report:
        report_path = args.report
    else:
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        report_path = os.path.join(repo_root, "samples", "report.example.json")

    if not os.path.exists(report_path):
        print(f"Report file not found: {report_path}")
        return

    report = load_sample_report(report_path)

    volumes = report.get("unused_volumes", [])
    buckets = report.get("buckets", [])

    output = {
        "unused_volumes": [
            {"VolumeId": v.get("VolumeId"), "Size": v.get("Size"), "State": v.get("State")}
            for v in volumes
        ],
        "monthly_waste_cost": calculate_cost(volumes),
        "buckets": buckets,
    }

    if args.delete:
        print("Delete requested, but destructive operations are disabled in local mode.")

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
