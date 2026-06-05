"""Simple janitor: detect unused EBS volumes and S3 buckets."""

import argparse
import json
import os
from typing import List

import boto3

try:  # support package and direct script execution
    from .constants import EBS_COST_PER_GB
except Exception:
    try:
        from constants import EBS_COST_PER_GB
    except Exception:
        EBS_COST_PER_GB = 0.08


def get_ec2_client():
    endpoint = os.getenv("LOCALSTACK_URL")
    region = os.getenv("AWS_REGION", "us-east-1")
    return boto3.client("ec2", region_name=region, endpoint_url=endpoint if endpoint else None)


def get_s3_client():
    endpoint = os.getenv("LOCALSTACK_URL")
    region = os.getenv("AWS_REGION", "us-east-1")
    return boto3.client("s3", region_name=region, endpoint_url=endpoint if endpoint else None)


def get_unused_volumes(ec2) -> List[dict]:
    resp = ec2.describe_volumes()
    volumes = resp.get("Volumes", [])
    return [v for v in volumes if v.get("State") == "available"]


def get_buckets(s3) -> List[str]:
    try:
        resp = s3.list_buckets()
        buckets = resp.get("Buckets", [])
        return [b.get("Name") for b in buckets]
    except Exception:
        return []


def calculate_cost(volumes: List[dict]) -> float:
    total = sum(v.get("Size", 0) * EBS_COST_PER_GB for v in volumes)
    return round(total, 2)


def delete_volumes(ec2, volumes: List[dict]) -> None:
    for v in volumes:
        vid = v.get("VolumeId")
        if not vid:
            continue
        try:
            ec2.delete_volume(VolumeId=vid)
        except Exception as e:
            print(f"Failed to delete {vid}: {e}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--delete", action="store_true", help="Delete unused volumes")
    args = parser.parse_args()

    print("Janitor started...")

    ec2 = get_ec2_client()
    s3 = get_s3_client()

    unused_volumes = get_unused_volumes(ec2)
    buckets = get_buckets(s3)

    output = {
        "unused_volumes": [
            {"VolumeId": v.get("VolumeId"), "Size": v.get("Size"), "State": v.get("State")}
            for v in unused_volumes
        ],
        "monthly_waste_cost": calculate_cost(unused_volumes),
        "buckets": buckets,
    }

    if args.delete:
        delete_volumes(ec2, unused_volumes)
        print("Deleted unused volumes")

    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
