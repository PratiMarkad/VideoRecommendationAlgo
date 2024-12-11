from api_helper import fetch_paginated_data
from preprocessing import (
    preprocess_video_data,
    preprocess_user_data,
    compute_similarity,
    recommend_videos,
)

# Mock API URL (replace with a real API if available)
VIDEO_API_URL = "https://api.videoservice.com/videos"
USER_DATA_FILE = "data/user_data.csv"  # Example CSV file path

def main():
    try:
        # Step 1: Fetch Video Data (Mock or API-based)
        print("Fetching video data...")
        video_data = fetch_paginated_data(VIDEO_API_URL)
        if not video_data:
            print("No video data retrieved. Exiting...")
            return

        # Step 2: Preprocess the Data
        print("Preprocessing video and user data...")
        video_data_df = preprocess_video_data(video_data)
        user_data_df = preprocess_user_data(USER_DATA_FILE)

        # Step 3: Compute Similarity and Recommend Videos
        print("Computing video recommendations...")
        similarity_df = compute_similarity(video_data_df, user_data_df)
        recommendations = recommend_videos(similarity_df)

        # Display Recommendations
        print("\nRecommended Videos:")
        print(recommendations)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
