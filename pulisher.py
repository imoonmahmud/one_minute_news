import requests
from config import FB_PAGE_ID, FB_PAGE_ACCESS_TOKEN

def post_photo_to_facebook(image_path: str, caption: str) -> dict:
    url = f"https://graph.facebook.com/{FB_PAGE_ID}/photos"

    with open(image_path, 'rb') as image_file:
        files = {'source': image_file}
        payload = {
            'caption': caption,
            'access_token': FB_PAGE_ACCESS_TOKEN
        }
        resp = requests.post(url, data=payload, files=files, timeout=60)

    print("Status:", resp.status_code)
    print("Response body:", resp.text)

    resp.raise_for_status()
    return resp.json()