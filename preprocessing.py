import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_video_data(video_data):
    """
    Convert video data to a pandas DataFrame and flatten tag lists.
    """
    # Convert the list of dictionaries into a DataFrame
    df = pd.DataFrame(video_data)
    
    # Flatten the 'tags' column: join lists into a single string
    if 'tags' in df.columns:
        df['tags'] = df['tags'].apply(lambda x: " ".join(x) if isinstance(x, list) else x)
    
    print("Processed Video Data:\n", df)
    return df

def preprocess_user_data(user_data_file):
    """
    Load and preprocess user data from a CSV file.
    """
    df = pd.read_csv(user_data_file)
    print("User Data Processed:\n", df)
    return df

def compute_similarity(video_df, user_df):
    """
    Compute similarity between user preferences and video tags.
    """
    print("Computing similarity between videos and user preferences...")

    # Merge all tags and preferences into a single column for each dataset
    video_tags = video_df['tags']
    user_preferences = user_df['preference']

    # Convert to simple text for mock similarity
    print("Video Tags:\n", video_tags)
    print("User Preferences:\n", user_preferences)

    # Mock similarity for demonstration
    similarity_data = {
        "user_id": [1, 2],
        "video_id": [1, 2],
        "score": [0.85, 0.76],
    }
    df = pd.DataFrame(similarity_data)
    print("Similarity Data:\n", df)
    return df

def recommend_videos(similarity_df):
    """
    Recommend top videos based on similarity scores.
    """
    print("Sorting videos based on similarity scores...")
    sorted_df = similarity_df.sort_values(by="score", ascending=False)
    return sorted_df.head(5)
