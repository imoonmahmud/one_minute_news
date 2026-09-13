from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
FB_PAGE_ID = os.getenv('FB_PAGE_ID')
FB_PAGE_ACCESS_TOKEN = os.getenv('FB_PAGE_ACCESS_TOKEN')