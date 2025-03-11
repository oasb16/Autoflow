# services/speech_agent.py
import boto3, requests
import openai
import uuid

class SpeechAgent:
    def __init__(self, aws_access_key, aws_secret_key, aws_region, openai_key):
        self.transcribe = boto3.client('transcribe', aws_access_key_id=aws_access_key,
                                       aws_secret_access_key=aws_secret_key, region_name=aws_region)
        self.polly = boto3.client('polly', aws_access_key_id=aws_access_key,
                                  aws_secret_access_key=aws_secret_key, region_name=aws_region)
        openai.api_key = openai_key

    def text_to_speech(self, text):
        response = self.polly.synthesize_speech(VoiceId='Joanna', OutputFormat='mp3', Text=text)
        audio_stream = response['AudioStream'].read()
        return audio_stream

    def speech_to_text(self, audio_uri):
        job_name = f"job-{uuid.uuid4()}"
        self.transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': audio_uri},
            MediaFormat='mp3',
            LanguageCode='en-US'
        )
        while True:
            status = self.transcribe.get_transcription_job(TranscriptionJobName=job_name)
            if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                break
        if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
            transcript_file_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
            transcript = requests.get(transcript_file_uri).json()['results']['transcripts'][0]['transcript']
            return transcript
        return None
