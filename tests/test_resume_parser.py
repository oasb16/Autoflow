# tests/test_resume_parser.py
import unittest
from services.resume_parser import ResumeParser

class TestResumeParser(unittest.TestCase):
    def setUp(self):
        self.parser = ResumeParser('aws_access_key', 'aws_secret_key', 'us-west-2')

    def test_parse_resume(self):
        sample_resume = b"Sample Resume Content"
        parsed_text = self.parser.parse_resume(sample_resume)
        self.assertIsInstance(parsed_text, str)