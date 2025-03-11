# utils/helpers.py
def sanitize_text(text):
    return text.strip().replace('\n', ' ').replace('\r', '')