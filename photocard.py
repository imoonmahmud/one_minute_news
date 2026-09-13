import html
from pathlib import Path
from playwright.sync_api import sync_playwright

TEMPLATE_PATH = Path('photocard_template.html')

def render_photocard(headline: str, source: str, image_url: str, output_path: str):
    template = TEMPLATE_PATH.read_text(encoding='utf-8')

    filled_html = (
        template
        .replace("{{HEADLINE}}", html.escape(headline))
        .replace("{{SOURCE}}", html.escape(source))
        .replace("{{IMAGE_URL}}", image_url)
    )

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            viewport={"width": 1080, "height": 1350},
            device_scale_factor=2
        )
        page.set_content(filled_html)
        page.wait_for_timeout(1000)

        actual_height = page.evaluate("document.body.scrollHeight")

        page.screenshot(
            path=output_path,
            clip={"x": 0, "y": 0, "width": 1080, "height": actual_height},
        )
        browser.close()

    print(f"Saveed: {output_path}")