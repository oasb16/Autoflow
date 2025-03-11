# tests/test_ats.py
import unittest
from services.ats_scoring import ATSScoring

class TestATSScoring(unittest.TestCase):
    def setUp(self):
        self.ats = ATSScoring('test_openai_key')

    def test_analyze_resume_match(self):
        resume_text = "Experienced Python developer"
        job_description = "Python developer needed"
        analysis = self.ats.analyze_resume_match(resume_text, job_description)
        self.assertIsInstance(analysis, str)

# tests/test_voice.py
import unittest
from services.speech_agent import SpeechAgent

class TestSpeechAgent(unittest.TestCase):
    def setUp(self):
        self.speech_agent = SpeechAgent('aws_access_key', 'aws_secret_key', 'us-west-2', 'test_openai_key')

    def test_text_to_speech(self):
        audio = self.speech_agent.text_to_speech("Hello world")
        self.assertIsInstance(audio, bytes)

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