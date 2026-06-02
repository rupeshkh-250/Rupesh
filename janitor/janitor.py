import boto3
import json
import argparse
import os

def get_ec2_client():
    return boto3.client(
        "ec2",
        region_name="us-east-1",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        endpoint_url=os.getenv("LOCALSTACK_URL", "http://localhost:4566")
    )

def get_s3_client():
    return boto3.client(
        "s3",
        region_name="us-east-1",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        endpoint_url=os.getenv("LOCALSTACK_URL", "http://localhost:4566")
    )

def get_unused_volumes(ec2):
    volscribe_volumes()umes = ec2.de["Volumes"]
    unused = [v for v in volumes if v["State"] == "available"]
    return unused

def get_buckets(s3):
    buckets = s3.list_buckets()["Buckets"]
    return [b["Name"] for b in buckets]

def calculate_cost(volumes):
    total = 0
    for v in volumes:
        total += v["Size"] * 0.08  # $0.08 per GB
    return round(total, 2)

def delete_volumes(ec2, volumes):
    for v in volumes:
        ec2.delete_volume(VolumeId=v["VolumeId"])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--delete", action="store_true")
    args = parser.parse_args()

    print("Janitor started...")

    ec2 = get_ec2_client()
    s3 = get_s3_client()

    unused_volumes = get_unused_volumes(ec2)
    buckets = get_buckets(s3)

    output = {
        "unused_volumes": [
            {
                "VolumeId": v["VolumeId"],
                "Size": v["Size"],
                "State": v["State"]
            }
            for v in unused_volumes
        ],
        "monthly_waste_cost": calculate_cost(unused_volumes),
        "buckets": buckets
    }

    if args.delete:
        delete_volumes(ec2, unused_volumes)
        print("Deleted unused volumes")

    print(json.dumps(output, indent=2))

if __name__ == "__main__":
    main()
