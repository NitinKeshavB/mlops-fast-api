try:
    import boto3
    from mypy_boto3_s3.client import S3Client
    from mypy_boto3_s3.type_defs import (
        PutObjectOutputTypeDef,
        ResponseMetadataTypeDef,
    )
except ImportError:
    raise ImportError("boto3 and mypy_boto3_s3 are required to use this module. Please install them via pip.")

bucket_name = "mlops-cloud-nk"
session = boto3.Session(profile_name="mlops")
s3_client: S3Client = session.client("s3")
response: PutObjectOutputTypeDef = s3_client.put_object(
    Bucket=bucket_name, Key="folder_1/test.txt", Body="hello world", ContentType="text/plain"
)

Metadata: ResponseMetadataTypeDef = response["ResponseMetadata"]

print(Metadata)
