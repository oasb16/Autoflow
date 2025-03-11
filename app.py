from flask import Flask, render_template, request, jsonify
from services.speech_agent import voice_interaction
from services.ats_scoring import analyze_resume_job_match
from services.job_fetcher import fetch_jobs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/voice-command', methods=['POST'])
def voice_command():
    audio_data = request.files['audio']
    response_text = voice_interaction(audio_data)
    return jsonify({"response": response_text})

@app.route('/apply', methods=['POST'])
def apply_job():
    resume = request.files['resume']
    job_id = request.form['job_id']
    result = analyze_resume_job_match(resume, job_id)
    return render_template('results.html', result=result)

@app.route('/jobs', methods=['GET'])
def jobs():
    jobs = fetch_jobs()
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=False)
