import requests
import random

UNSPLASH_ACCESS_KEY = "gkc0L8FvC83uYNyvBnYkZ0D2l331pYR1tzPZA5Rgzm8"
SEARCH_URL = "https://api.unsplash.com/search/photos"

def fetch_ice_cream_image():
    params = {
        "query": "ice cream",
        "client_id": UNSPLASH_ACCESS_KEY,
        "per_page": 30,
        "orientation": "squarish"
    }
    response = requests.get(SEARCH_URL, params=params)
    response.raise_for_status()
    results = response.json()
    image_urls = [img["urls"]["regular"] for img in results.get("results", [])]
    return random.choice(image_urls) if image_urls else None
