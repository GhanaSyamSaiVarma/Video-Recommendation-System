# 1. config.py
import os

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