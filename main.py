import os
import time
from scraper import get_treanding_articles, get_article_text, get_article_image
from database import init_db, already_posted, mark_posted
from rewrite import rewrite
from photocard import render_photocard
from pulisher import post_photo_to_facebook

OUTPUT_DIR = 'generated_cards'
DELAY_BETWEEN_POSTS = 10 * 60

def run():
    conn = init_db()
    articles = get_treanding_articles()

    posted_this_run = 0

    for i, art in enumerate(articles):
        if already_posted(conn, art['link']):
            print("Already posted, skipping:", art['title'])
            continue

        body = get_article_text(art['link'])
        post_text = rewrite(art['title'], body)
        image_url = get_article_image(art['link'])

        card_path = os.path.join(OUTPUT_DIR, f"card_{i}.png")
        render_photocard(
            headline=art["title"],
            source="Prothom Alo",
            image_url=image_url,
            output_path=card_path,
        )

        print("--- Draft Post ---")
        print(post_text)
        print("Card saved:", card_path)

        result = post_photo_to_facebook(card_path, post_text)
        print('Posted to Facebook:', result)
        print()

        mark_posted(conn, art['link'], art['title'])
        posted_this_run += 1

        if posted_this_run < len(articles):
            time.sleep(DELAY_BETWEEN_POSTS)

if __name__ == '__main__':
    run()