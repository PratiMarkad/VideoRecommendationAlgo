import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate

def content_based_recommendations(tfidf_matrix, index, top_n=5):
    """Content-based recommendations using cosine similarity."""
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    similar_indices = cosine_sim[index].argsort()[:-top_n-1:-1]
    return similar_indices

def collaborative_filtering_ratings(ratings_df):
    """Collaborative filtering using SVD from Surprise."""
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings_df[["user_id", "video_id", "rating"]], reader)
    model = SVD()
    cross_validate(model, data, cv=5)
    return model

if __name__ == "__main__":
    posts_df = pd.read_csv("data/preprocessed_posts.csv")
    tfidf_matrix = compute_tfidf_similarity(posts_df)
    recommendations = content_based_recommendations(tfidf_matrix, index=0)
    print("Recommended video indices:", recommendations)
