
# apna poora code yaha paste karo

import requests
import json
from datetime import datetime

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
response = requests.get(url)

story_ids = response.json()[:500]

all_stories = []

for story_id in story_ids:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    res = requests.get(story_url)
    data = res.json()

    if not data or "title" not in data:
        continue

    story = {
        "post_id": data.get("id"),
        "title": data.get("title"),
        "score": data.get("score", 0),
        "num_comments": data.get("descendants", 0),
        "author": data.get("by", ""),
        "collected_at": datetime.now().isoformat()
    }

    all_stories.append(story)

file_name = datetime.now().strftime("%Y%m%d")

with open(f"trends_{file_name}.json", "w") as f:
    json.dump(all_stories, f, indent=4)
