# tests/test_voice.py
import unittest
from services.speech_agent import SpeechAgent

class TestSpeechAgent(unittest.TestCase):
    def setUp(self):
        self.speech_agent = SpeechAgent('aws_access_key', 'aws_secret_key', 'us-west-2', 'test_openai_key')

    def test_text_to_speech(self):
        audio = self.speech_agent.text_to_speech("Hello world")
        self.assertIsInstance(audio, bytes)