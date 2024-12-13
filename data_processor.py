# 2. data_processor.py
import requests
import pandas as pd
import numpy as np
from typing import Dict, List
from config import Config

class DataProcessor:
    def __init__(self):
        self.headers = {
            "Flic-Token": Config.FLIC_TOKEN
        }

    def fetch_paginated_data(self, endpoint: str, page_size: int = 1000) -> List[Dict]:
        """
        Fetch paginated data from a given API endpoint
        """
        all_data = []
        page = 1

        while True:
            params = {
                "page": page,
                "page_size": page_size,
                "resonance_algorithm": "resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if"
            }
            
            response = requests.get(endpoint, headers=self.headers, params=params)
            
            if response.status_code != 200:
                break
            
            data = response.json()
            if not data:
                break
            
            all_data.extend(data)
            page += 1

        return all_data

    def preprocess_data(self, data: List[Dict]) -> pd.DataFrame:
        """
        Preprocess raw data into a structured DataFrame
        """
        df = pd.DataFrame(data)
        
        # Handle missing values
        df.fillna({
            'views': 0,
            'likes': 0,
            'ratings': 0,
            'category': 'Unknown'
        }, inplace=True)
        
        return df