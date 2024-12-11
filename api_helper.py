import requests

def fetch_data(url, params=None):
    """
    Fetch data from the given API URL with error handling.
    """
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP error codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def fetch_paginated_data(base_url, pages=1):
    """
    Fetch paginated video data. Uses mock data if API fails.
    """
    all_data = []
    for page in range(1, pages + 1):
        print(f"Fetching page {page}...")
        url = f"{base_url}?page={page}"
        data = fetch_data(url)

        if data:  # Add real API data
            all_data.extend(data)
        else:
            print("Using mock data as fallback...")
            all_data = [
                {"video_id": 1, "title": "Sample Video 1", "tags": ["music", "fun"]},
                {"video_id": 2, "title": "Sample Video 2", "tags": ["tech", "education"]},
            ]
            break  # Stop pagination for mock data

    return all_data
