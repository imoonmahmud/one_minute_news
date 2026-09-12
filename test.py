from rewrite import rewrite
from scraper import get_article_text

url = "https://www.prothomalo.com/bangladesh/district/0o8h7skjj3"
body = get_article_text(url)
result = rewrite("স্রোতে তলিয়ে যাচ্ছিলেন পাঁচজন...", body)
print(result)