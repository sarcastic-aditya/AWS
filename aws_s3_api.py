def S3bucket():
    import boto3
    import uuid
# AWS access keys
    access_key = 'Write your access'
    secret_key ='Your secret key'
# AWS region
    region = 'ap-south-1b'  # Replace with your desired region

# Create an S3 client using access keys
    s3_client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    # S3 bucket name
    myuuid=uuid.uuid1().int
    bucket_name = 'Bucket'+str(myuuid)  # Replace with your desired bucket name

# Create an S3 bucket
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    # Print the bucket creation confirmation
    print(f"Bucket '{bucket_name}' created successfully.")