# import requests
# from bs4 import BeautifulSoup

# url = "https://www.prothomalo.com/bangladesh/district/0o8h7skjj3"
# headers = {"User-Agent": "Mozilla/5.0"}

# resp = requests.get(url, headers=headers, timeout=15)
# soup = BeautifulSoup(resp.text, 'html.parser')

# og_image = soup.find('meta', property='og:image')
# print("Image URL:", og_image['content'] if og_image else "not found")


from photocard import render_photocard

render_photocard(
    headline="স্রোতে তলিয়ে যাচ্ছিলেন পাঁচজন, ঝাঁপ দিয়ে দুজনকে উদ্ধার করে মারা গেলেন তরুণ",
    source="Prothom Alo",
    image_url="https://media.prothomalo.com/prothomalo-bangla%2F2026-09-12%2F08zr6wej%2FNarsingdi1.jpg?rect=0%2C68%2C1600%2C840&w=1200&ar=40%3A21&auto=format%2Ccompress",
    output_path="test_card.png",
)