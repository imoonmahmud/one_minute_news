from scraper import get_treanding_articles, get_article_text
from database import init_db, already_posted, mark_posted

def run():
    conn = init_db()
    articles = get_treanding_articles()

    for art in articles:
        if already_posted(conn, art['link']):
            print("Already posted, skipping:", art['title'])
            continue

        body = get_article_text(art['link'])
        print("Would post:", art['title'])
        print("Body preview:", body[:120])
        print()


        mark_posted(conn, art['link'], art['title'])


if __name__ == '__main__':
    run()