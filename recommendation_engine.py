# 3. recommendation_engine.py
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

class RecommendationEngine:
    def __init__(self, user_data: pd.DataFrame, post_data: pd.DataFrame):
        self.user_data = user_data
        self.post_data = post_data
        
        # Content-based features preparation
        self.prepare_content_features()
        
        # Collaborative filtering preparation
        self.prepare_collaborative_features()

    def prepare_content_features(self):
        """
        Prepare content-based features using TF-IDF
        """
        # Use text features for content similarity
        tfidf = TfidfVectorizer(stop_words='english')
        self.content_matrix = tfidf.fit_transform(self.post_data['description'].fillna(''))
        self.content_similarity = cosine_similarity(self.content_matrix)

    def prepare_collaborative_features(self):
        """
        Prepare collaborative filtering features
        """
        # Create user-post interaction matrix
        self.interaction_matrix = pd.pivot_table(
            self.user_data, 
            values='engagement_score', 
            index='username', 
            columns='post_id', 
            fill_value=0
        )

    def recommend_posts(self, username: str, category_id: str = None, mood: str = None, top_n: int = 10):
        """
        Hybrid recommendation method
        """
        # 1. Collaborative Filtering Component
        try:
            user_interactions = self.interaction_matrix.loc[username]
            similar_user_posts = user_interactions[user_interactions > 0].index.tolist()
        except KeyError:
            # Cold start: recommend popular posts
            similar_user_posts = self.post_data.nlargest(top_n, 'views')['post_id'].tolist()

        # 2. Content-Based Component
        if category_id:
            category_posts = self.post_data[self.post_data['category_id'] == category_id]
        else:
            category_posts = self.post_data

        # 3. Mood-Based Filtering (if applicable)
        if mood:
            mood_posts = category_posts[category_posts['mood_tags'].str.contains(mood, case=False, na=False)]
        else:
            mood_posts = category_posts

        # Combine and rank recommendations
        recommendations = []
        for post_id in similar_user_posts:
            if post_id in mood_posts['post_id'].values:
                post_details = self.post_data[self.post_data['post_id'] == post_id]
                recommendations.append(post_details)
                
                if len(recommendations) == top_n:
                    break

        return pd.concat(recommendations).head(top_n)