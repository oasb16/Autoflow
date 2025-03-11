// static/scripts.js
document.addEventListener('DOMContentLoaded', () => {
    const startVoiceBtn = document.getElementById('start-voice');
    const applyForm = document.getElementById('apply-form');
    const applicationResult = document.getElementById('application-result');

    startVoiceBtn.addEventListener('click', () => {
        alert('Voice interaction feature coming soon!');
    });

    applyForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(applyForm);
        const response = await fetch('/apply', {
            method: 'POST',
            body: formData
        });
        const resultHTML = await response.text();
        applicationResult.innerHTML = resultHTML;
    });
});