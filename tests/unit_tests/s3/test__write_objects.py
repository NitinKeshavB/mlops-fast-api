"""Test cases for `s3.write_objects`."""

import boto3

from files_api.s3.write_objects import upload_s3_object
from tests.consts import TEST_BUCKET_NAME


# pylint: disable=unused-argument
def test_upload_s3_object(mocked_aws):
    """Test that upload_s3_object uploads a file to S3 successfully."""
    file_content = b"test content"
    object_key = "testfile.txt"
    content_type = "text/plain"
    upload_s3_object(
        TEST_BUCKET_NAME,
        object_key=object_key,
        file_content=file_content,
        content_type=content_type,
    )

    s3_client = boto3.client("s3")
    response = s3_client.get_object(Bucket=TEST_BUCKET_NAME, Key=object_key)
    assert response["Body"].read() == file_content
    assert response["ContentType"] == content_type
