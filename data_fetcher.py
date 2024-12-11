import requests
import pandas as pd

FLIC_TOKEN = "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"
HEADERS = {"Flic-Token": FLIC_TOKEN}

BASE_URLS = {
    "viewed": "https://api.socialverseapp.com/posts/view",
    "liked": "https://api.socialverseapp.com/posts/like",
    "inspired": "https://api.socialverseapp.com/posts/inspire",
    "rated": "https://api.socialverseapp.com/posts/rating",
    "posts": "https://api.socialverseapp.com/posts/summary/get",
}

def fetch_data(api_name, page_size=1000):
    """Fetch paginated data from the given API."""
    data = []
    page = 1
    while True:
        url = f"{BASE_URLS[api_name]}?page={page}&page_size={page_size}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}")
            break
        
        # Print the raw response to debug
        print(f"Response for {api_name}, page {page}: {response.json()}")
        
        batch = response.json()
        
        # Check if 'data' key exists in the response
        if "data" not in batch:
            print(f"Warning: 'data' key not found in response from {api_name}, page {page}")
            break
            
        if not batch["data"]:
            break
        
        data.extend(batch["data"])
        page += 1
    print(f"Fetched {len(data)} records from {api_name} API.")
    return pd.DataFrame(data)


if __name__ == "__main__":
    # Test the API fetcher
    viewed_data = fetch_data("viewed")
    liked_data = fetch_data("liked")
    viewed_data.to_csv("data/viewed_posts.csv", index=False)
    liked_data.to_csv("data/liked_posts.csv", index=False)
