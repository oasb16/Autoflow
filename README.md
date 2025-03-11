# Hands-Free Job Application Assistant

## Overview

A fully automated, voice-driven job application system built with Python Flask, integrated with AWS and OpenAI services to simplify and optimize the job search and application process.

## Features
- Hands-free interaction via voice using AWS Transcribe and Polly
- AI-driven ATS scoring and resume analysis powered by OpenAI
- Resume parsing using AWS Textract
- Secure resume storage with AWS S3
- Robust frontend built with Flask templates
- Comprehensive unit testing for reliability

## Project Structure
```
voice_job_agent/
├── app.py                       # Flask application entry-point
├── config.py                    # Configuration and credentials
├── services/
│   ├── ats_scoring.py
│   ├── speech_agent.py
│   ├── job_fetcher.py
│   ├── resume_parser.py
│   └── storage.py
├── utils/
│   └── helpers.py               # Utility functions
├── templates/
│   ├── index.html               # Main landing page
│   └── results.html             # ATS scoring results
├── static/
│   ├── styles.css
│   └── scripts.js
├── tests/
│   ├── test_ats.py
│   ├── test_voice.py
│   └── test_resume_parser.py
├── requirements.txt
├── runtime.txt
├── Procfile
└── README.md
```

## Setup Instructions

### Requirements
- Python 3.12
- AWS Account with IAM permissions (S3, Polly, Textract, Transcribe)
- OpenAI API key

### Installation
```bash
pip install -r requirements.txt
```

### Environment Variables
Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_api_key
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_KEY=your_aws_secret_key
AWS_REGION=your_aws_region
BUCKET_NAME=your_s3_bucket_name
JOB_API_ENDPOINT=your_job_api_endpoint
```

### Running Locally
```bash
python app.py
```

### Deploying to Heroku
1. Log in to Heroku CLI and initialize the repository:
```bash
heroku login
git init
heroku create your-app-name
```

2. Set Heroku environment variables:
```bash
heroku config:set OPENAI_API_KEY=your_openai_api_key AWS_ACCESS_KEY=your_aws_access_key AWS_SECRET_KEY=your_aws_secret_key AWS_REGION=your_aws_region BUCKET_NAME=your_s3_bucket_name JOB_API_ENDPOINT=your_job_api_endpoint
```

3. Deploy:
```bash
git add .
git commit -m "Deploy app"
git push heroku main
```

## Testing
Run tests using:
```bash
python -m unittest discover tests
```

## License
MIT
