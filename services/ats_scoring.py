# services/ats_scoring.py
import openai

class ATSScoring:
    def __init__(self, openai_key):
        openai.api_key = openai_key

    def analyze_resume_match(self, resume_text, job_description):
        response = openai.chat.completions.create(
            model="gpt-4o-turbo",
            messages=[
                {"role": "system", "content": "You are an expert ATS analyzer. Provide a detailed ATS compatibility score and suggestions."},
                {"role": "user", "content": f"Resume: {resume_text}\n\nJob Description: {job_description}"}
            ]
        )
        analysis = response.choices[0].message.content
        return analysis
