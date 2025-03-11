# services/resume_parser.py
import boto3

class ResumeParser:
    def __init__(self, aws_access_key, aws_secret_key, aws_region):
        self.textract_client = boto3.client(
            'textract',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region
        )

    def parse_resume(self, resume_bytes):
        response = self.textract_client.detect_document_text(Document={'Bytes': resume_bytes})
        extracted_text = " ".join([item["DetectedText"] for item in response["Blocks"] if item["BlockType"] == "LINE"])
        return extracted_text