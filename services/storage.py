import boto3
from botocore.exceptions import NoCredentialsError, ClientError

class StorageService:
    def __init__(self, aws_access_key, aws_secret_key, aws_region, bucket_name):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region
        )
        self.bucket_name = bucket_name

    def upload_file(self, file_bytes, file_name, content_type='application/pdf'):
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=file_bytes,
                ContentType=content_type,
                ACL='private'
            )
            file_url = f"https://{self.bucket_name}.s3.{self.s3_client.meta.region_name}.amazonaws.com/{file_name}"
            return file_url
        except (NoCredentialsError, ClientError) as e:
            print(f"Error uploading file: {e}")
            return None

    def download_file(self, file_name):
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=file_name)
            return response['Body'].read()
        except ClientError as e:
            print(f"Error downloading file: {e}")
            return None

    def delete_file(self, file_name):
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=file_name)
            return True
        except ClientError as e:
            print(f"Error deleting file: {e}")
            return False

    def list_files(self, prefix=''):
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
            if 'Contents' in response:
                return [item['Key'] for item in response['Contents']]
            return []
        except ClientError as e:
            print(f"Error listing files: {e}")
            return []
