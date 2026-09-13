from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup

def get_treanding_articles():
    url = "https://www.prothomalo.com/"
    articles = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=30000)
        page.wait_for_timeout(3000)

        try:
            page.click('text=OK', timeout=5000)
        except Exception:
            pass
        page.wait_for_timeout(1000)

        for _ in range(8):
            page.mouse.wheel(0, 800)
            page.wait_for_timeout(500)

        tab = page.query_selector("h2.tab-headline:has-text('আলোচিত')")
        tab.click()
        page.wait_for_timeout(1500)

        items = page.query_selector_all("div.numbered-story-headline-wrapper a")
        for item in items[:5]:
            articles.append({
                'title': item.inner_text().strip(),
                'link': item.get_attribute('href')
            })

        browser.close()

    return articles


def get_article_text(url: str) -> str:
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(resp.text, "html.parser")

    paragraphs = soup.find_all("p")
    body_text = " ".join(p.get_text().strip() for p in paragraphs)
    return body_text


def get_article_image(url: str) -> str | None:
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=15)
    soup = BeautifulSoup(resp.text, "html.parser")

    og_image = soup.find("meta", property="og:image")
    if og_image:
        url = og_image["content"]
        return url.split("&overlay=")[0]
    return None