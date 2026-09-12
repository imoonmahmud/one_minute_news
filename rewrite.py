import requests
from config import API_KEY

MODEL = "gemini-3.1-flash-lite"
PROMPT_TEMPLATE = """Rewrite this news item as a short, engaging Facebook post in Bengali.
Rules:
- 40-60 words max
- Neutral, factual tone, no clickbait
- Do not copy sentences from the original — full rewrite in your own words
- End with a short question or takeaway to encourage engagement

Headline: {title}
Article: {body}
"""

def rewrite(title: str, body: str) -> str:
    prompt = PROMPT_TEMPLATE.format(title=title, body=body[:2000])
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    
    resp = requests.post(
        url,
        json={"contents": [{"parts": [{"text": prompt}]}]},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["candidates"][0]["content"]["parts"][0]["text"].strip()