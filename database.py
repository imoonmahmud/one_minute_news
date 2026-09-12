import sqlite3

def init_db():
    conn = sqlite3.connect('posted_articles.db')
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posted (
            link TEXT PRIMARY KEY,
            title TEXT,
            posted_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn

def already_posted(conn, link: str) -> bool:
    cur = conn.execute("SELECT 1 FROM posted WHERE link = ?", (link,))
    return cur.fetchone() is not None

def mark_posted(conn, link: str, title: str):
    conn.execute("INSERT INTO posted (link, title) VALUES (?, ?)", (link, title))
    conn.commit()