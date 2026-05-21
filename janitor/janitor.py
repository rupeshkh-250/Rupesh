import boto3
import json
import sys

# Config
EBS_PRICE_PER_GB = 0.08  # per GB/month
EC2_T3_MICRO = 8.0       # approx monthly cost

# Dry run logic
DRY_RUN = True
if "--delete" in sys.argv:
    DRY_RUN = False

print(f"Dry run mode: {DRY_RUN}")


def get_ec2_client():
    return boto3.client(
        "ec2",
        region_name="us-east-1",
        endpoint_url="http://localhost:4566",
        aws_access_key_id="test",
        aws_secret_access_key="test"
    )


def get_s3_client():
    return boto3.client(
        "s3",
        endpoint_url="http://localhost:4566",
        aws_access_key_id="test",
        aws_secret_access_key="test"
    )


def get_unused_volumes(ec2):
    response = ec2.describe_volumes()
    unused = []

    for vol in response["Volumes"]:
        if vol["State"] == "available":
            unused.append({
                "VolumeId": vol["VolumeId"],
                "Size": vol["Size"],
                "State": vol["State"]
            })

    return unused


def delete_volumes(ec2, volumes):
    for vol in volumes:
        vid = vol["VolumeId"]
        print(f"Deleting volume: {vid}")
        ec2.delete_volume(VolumeId=vid)


def calculate_cost(volumes):
    total = 0
    for vol in volumes:
        total += vol["Size"] * EBS_PRICE_PER_GB
    return total


def get_buckets(s3):
    response = s3.list_buckets()
    return [b["Name"] for b in response["Buckets"]]


def main():
    ec2 = get_ec2_client()
    s3 = get_s3_client()

    output = {}

    # Volumes
    unused_volumes = get_unused_volumes(ec2)
    output["unused_volumes"] = unused_volumes

    # Cost
    total_cost = calculate_cost(unused_volumes)
    output["monthly_waste_cost"] = total_cost

    # Buckets
    buckets = get_buckets(s3)
    output["buckets"] = buckets

    # Delete if needed
    if not DRY_RUN:
        delete_volumes(ec2, unused_volumes)

    # Final output
    print(json.dumps(output, indent=2, default=str))


# Entry point (VERY IMPORTANT)
if __name__ == "__main__":
    main()