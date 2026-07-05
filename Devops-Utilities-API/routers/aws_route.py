from fastapi import APIRouter, HTTPException
from services.aws_service import get_bucket_info, get_instances_info

router = APIRouter()

@router.get("/s3", status_code=200)

def get_aws_bucket():

    try:
        buckets_info = get_bucket_info()
        return buckets_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

@router.get("/ec2", status_code=200)

def get_instances():

    try:
        instance_info = get_instances_info()
        return instance_info
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
