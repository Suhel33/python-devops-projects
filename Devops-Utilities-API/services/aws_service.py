import boto3 
from datetime import datetime, timezone, timedelta

def get_bucket_info():
    s3_client = boto3.client("s3")

    buckets = s3_client.list_buckets()["Buckets"]

    new_buckets = []
    old_buckets = []
    current_date = datetime.now(timezone.utc).astimezone()      # current date = 13-06-2026  June
    print("Current Date : ",current_date)

    days = int(input("How Many Days Ago : "))         # How Many Days Ago : 50
    days_ago = current_date - timedelta(days=days)    # Aaj Se 50 days ago = 24-04-2026  April
    print(f"{days} Days Ago Date & Time : {days_ago}")
    
    for bucket in buckets:
        bucket_name = bucket["Name"]
        creation_date = bucket["CreationDate"]          # creation date = 08-06-2026  June  |  10-04-2026 April
        print("Creation Date : ",creation_date, "Bucket Name : " + bucket_name)
        if creation_date < days_ago:        # {08-06-2026  June} < {24-04-2026  April} ---> False  (New Bucket Create) | {10-04-2026 April} < {24-04-2026  April} ---> True (Old Bucket Create)
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)
    
    return {
        "total_buckets":len(buckets),
        "new_buckets":len(new_buckets),
        "old_buckets":len(old_buckets),
        "new_buckets_names":new_buckets,
        "old_buckets_names":old_buckets
    }

# EC2 Instances

def get_instances_info():
    ec2_client = boto3.client("ec2")
    instances = ec2_client.describe_instances()

    new_instances = []
    old_instances = []

    current_date = datetime.now(timezone.utc).astimezone()      # current date = 13-06-2026  June
    print("Current Date : ",current_date)

    days = int(input("How Many Days Ago : "))         # How Many Days Ago : 50
    days_ago = current_date - timedelta(days=days)    # Aaj Se 50 days ago = 24-04-2026  April
    print(f"{days} Days Ago Date & Time : {days_ago}")

    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:

            creation_launchtime = instance.get("LaunchTime")
            print("Creation LaunchTime : ", creation_launchtime)
            if creation_launchtime < days_ago:
                old_instances.append({
                    "Instance Tags" : instance["Tags"],
                    "instance ID" : instance["InstanceId"],
                    "State" : instance["State"]["Name"],
                    "LaunchTime" : instance.get("LaunchTime")
                })
            
            else:
                new_instances.append({
                    "Instance Tags" : instance["Tags"],
                    "instance ID" : instance["InstanceId"],
                    "State" : instance["State"]["Name"],
                    "LaunchTime" : instance.get("LaunchTime")
                })

    return{
        "total_instances":(len(old_instances) + len(new_instances)),
        "new instances":len(new_instances),
        "old instances":len(old_instances),
        "new instances_names":new_instances,
        "old instances_names":old_instances,
    }
