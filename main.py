import requests
import time

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url)
ids = response.json()

for i, id in enumerate(ids[:30], 1):
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    item_response = requests.get(item_url)
    story_data = item_response.json()

    title = story_data.get("title")
    link = story_data.get("url")

    if link is None:
        continue
    time.sleep(1)
    print(f"{{'title': '{title}', 'link': '{link}'}}")
