import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_REGION = 'us-west-2'

BUCKET_NAME = 'your-s3-bucket-name'
JOB_API_ENDPOINT = 'https://your-api-gateway.execute-api.us-west-2.amazonaws.com/prod/jobs'
