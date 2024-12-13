# app.py
from flask import Flask, request, jsonify
import requests
import pandas as pd
import logging
from flask_cors import CORS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Config:
    API_BASE_URL = "https://api.socialverseapp.com"
    FLIC_TOKEN = "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"
    
    # API Endpoints
    POSTS_VIEW_ENDPOINT = f"{API_BASE_URL}/posts/view"
    POSTS_LIKE_ENDPOINT = f"{API_BASE_URL}/posts/like"
    POSTS_INSPIRE_ENDPOINT = f"{API_BASE_URL}/posts/inspire"
    POSTS_RATING_ENDPOINT = f"{API_BASE_URL}/posts/rating"
    POSTS_SUMMARY_ENDPOINT = f"{API_BASE_URL}/posts/summary/get"
    USERS_ENDPOINT = f"{API_BASE_URL}/users/get_all"

class DataProcessor:
    @staticmethod
    def fetch_mock_data():
        """
        Generate mock data when API is unavailable
        """
        # Mock user data
        users = pd.DataFrame({
            'username': ['user1', 'user2', 'user3'],
            'engagement_score': [0.8, 0.6, 0.7]
        })

        # Mock post data
        posts = pd.DataFrame({
            'post_id': ['post1', 'post2', 'post3', 'post4', 'post5'],
            'description': [
                'Motivational speech about success',
                'Fitness and health tips',
                'Personal development strategies',
                'Entrepreneurship insights',
                'Mental health awareness'
            ],
            'category_id': ['motivation', 'fitness', 'personal-dev', 'business', 'mental-health'],
            'views': [1000, 800, 1200, 950, 750],
            'mood_tags': ['inspiring', 'energetic', 'positive', 'ambitious', 'calm']
        })

        return users, posts

    @staticmethod
    def fetch_data(endpoint, headers):
        """
        Attempt to fetch data from API with error handling
        """
        try:
            response = requests.get(
                endpoint, 
                headers=headers, 
                timeout=10  # 10-second timeout
            )
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except (requests.RequestException, ValueError) as e:
            logger.warning(f"Error fetching data from {endpoint}: {e}")
            return None

class RecommendationEngine:
    def recommend_posts(self, username, category_id=None, mood=None, top_n=10):
        """
        Mock recommendation method
        """
        users, posts = DataProcessor.fetch_mock_data()
        
        if category_id:
            posts = posts[posts['category_id'] == category_id]
        
        if mood:
            posts = posts[posts['mood_tags'].str.contains(mood, case=False, na=False)]
        
        # Simple recommendation logic
        recommended_posts = posts.nlargest(top_n, 'views')
        return recommended_posts

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes

    recommendation_engine = RecommendationEngine()

    @app.route('/feed', methods=['GET'])
    def get_recommendations():
        username = request.args.get('username', 'default_user')
        category_id = request.args.get('category_id')
        mood = request.args.get('mood')

        recommendations = recommendation_engine.recommend_posts(
            username, 
            category_id=category_id, 
            mood=mood
        )

        return jsonify(recommendations.to_dict(orient='records'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)