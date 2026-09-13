import requests
from config import API_KEY

MODEL = "gemini-3.1-flash-lite"
FEWSHOT_EXAMPLES = """গতকালকে আমরা দেখেছি অফিশিয়ালি রিলিজ হলো iPhone 18 সিরিজ এবং প্রথম তারা ফোল্ডেবল ফোন নিয়ে এসেছে এবং এগুলো আসলে কেমন হবে আমাদের জন্য বা নতুনত্ব কি আছে নিশ্চয়ই অনেকে আমরা জানতে চাই ঠিক যতটুকু জানলাম তাদের লঞ্চিং ইভেন্ট থেকে সেটাই জানানোর চেষ্টা করেছি চরণ আমরা বিষয়গুলো জানি এবং হয়তো আমরা কিছুদিন পর বাংলাদেশেও এই ফোন গুলো দেখতে পাব।

নেত্রকোণার একটি পৌরসভায় জনসাধারণের ব্যবহারের জন্য সংগৃহীত শত শত ডাস্টবিন দুই বছরেরও বেশি সময় ধরে অব্যবহৃত পড়ে আছে। বিতরণ না করে এভাবে ফেলে রাখার বিষয়ে ক্ষোভ প্রকাশ করেছেন নেত্রকোণা-৪ আসনের সংসদ সদস্য ও সাবেক স্বরাষ্ট্র প্রতিমন্ত্রী লুৎফুজ্জামান বাবর, আরো বিস্তারিত কমেন্টে।

শিক্ষা বোর্ডের দায়িত্বশীল কর্মকর্তাদের ভাষ্যমতে, পুনর্নিরীক্ষণ প্রক্রিয়ার ইতিহাসে এত বিপুলসংখ্যক শিক্ষার্থীর ফলাফলে পরিবর্তন আসার নজির অতীতে আর কখনো দেখা যায়নি, এবং অনেক শিক্ষার্থীর আনন্দিত তাদের রেজাল্ট পরিবর্তন হওয়াতে।

সিঙ্গাপুরে বিমানবন্দরে এখন ইমিগ্রেশন সম্পূর্ণ স্বয়ংক্রিয়—বাংলাদেশসহ বিশ্বের যেকোনো দেশের পর্যটকরা কোনো পূর্বনিবন্ধন বা বাড়তি ঝামেলা ছাড়াই সরাসরি অটোমেটিক গেট ব্যবহার করতে পারছেন। তবে এর জন্য আসার ৩ দিন আগে অনলাইনে বিনামূল্যে SG Arrival Card (SGAC) পূরণ করে নিতে হবে। বিমানবন্দরে নামার পর শুধু পাসপোর্ট স্ক্যান করলেই ক্যামেরা ও স্ক্যানার আপনার ফেস ও আইরিস স্বয়ংক্রিয়ভাবে যাচাই করে নেবে, আর সঙ্গে সঙ্গে খুলে যাবে গেট। কোনো লাইন নেই, কোনো কর্মকর্তার প্রয়োজন নেই—পুরো প্রক্রিয়া শেষ হয়ে যায় মাত্র কয়েক সেকেন্ডে।

আগামী শিক্ষাবর্ষ থেকে বড় একটা পরিবর্তন আসছে আমাদের পাঠ্যবইয়ে! মাননীয় প্রধানমন্ত্রীর শিক্ষা উপদেষ্টা মাহদী আমিন জানিয়েছেন, ষষ্ঠ থেকে অষ্টম শ্রেণির বইয়ে এখন থেকে থাকবে আর্টিফিশিয়াল ইন্টেলিজেন্স, রোবোটিক্স, মেশিন লার্নিং আর সাইবার সিকিউরিটির মতো একদম আধুনিক বিষয়। মানে আমাদের ছোট ভাই-বোনরা এখন থেকেই টেক-স্কিল শিখবে স্কুল থেকে! ভবিষ্যৎ প্রজন্মকে প্রযুক্তিনির্ভর করে গড়ে তোলার এই পদক্ষেপ কতটা কার্যকর হয়, সেটাই এখন দেখার বিষয়।"""

PROMPT_TEMPLATE = """You write short Facebook news posts in casual, conversational Bangla for a Bangladeshi audience. Study these example posts carefully — match their tone, sentence rhythm, and structure exactly:

{examples}

Style notes:
- Conversational, slightly informal register — not stiff "news anchor" Bangla
- Third-person narration ("তিনি জানান", "জানা গেছে") mixed with a natural, flowing single-paragraph style
- Break the post into 2-3 short paragraphs separated by a blank line — never one dense unbroken block of text. Each paragraph should cover one beat of the story (what happened, then the consequence/reaction, etc.)
- Occasionally end with a soft hook like "আরো বিস্তারিত কমেন্টে" or a forward-looking line ("...সেটাই এখন দেখার বিষয়") — vary it, don't reuse the same ending every time
- No hashtags, no clickbait phrasing, no emoji
- Do not copy sentences from the source article — full rewrite in your own words
- Length: roughly 60-100 words

Now write one in this style for the following news item:

Headline: {title}
Article: {body}
"""

def rewrite(title: str, body: str) -> str:
    prompt = PROMPT_TEMPLATE.format(examples=FEWSHOT_EXAMPLES, title=title, body=body[:2000])
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
    
    resp = requests.post(
        url,
        json={"contents": [{"parts": [{"text": prompt}]}]},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["candidates"][0]["content"]["parts"][0]["text"].strip()