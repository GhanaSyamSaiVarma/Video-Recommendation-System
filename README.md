# 🎥 Video Recommendation System

## 🎯 Objective

Design a recommendation algorithm that suggests videos based on user preferences and engagement patterns. The algorithm will deliver personalized video recommendations by leveraging user interaction data and video metadata obtained via provided APIs.

## 📊 Dataset

The dataset can be fetched using the following APIs, which provide information on user interactions and video metadata: 
Make sure using using pagination to fetch data and managing the data fetching method in a way that it's not fetching same data again and again.

### APIs

1. **Get All Viewed Posts** (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/view?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```

2. **Get All Liked Posts** (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/like?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```

3. **Get All Inspired posts** (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/inspire?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```


4. **Get All Rated posts** (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/rating?page=1&page_size=1000&resonance_algorithm=resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if
   ```

5. **Get All Posts** (Header required*) (METHOD: GET):
   ```
   https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000
   ```

6. **Get All Users** (Header required*) (METHOD: GET):
   ```
   https://api.socialverseapp.com/users/get_all?page=1&page_size=1000
   ```

### Authorization

For autherization pass `Flic-Token` as header in the API request:

Header:
```json
"Flic-Token": "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"
```

### Requirements

1. **Personalization:** The recommendation algorithm should make personalized suggestions based on user history and engagement patterns.
2. **Cold Start Problem Handling:** Include a mechanism to recommend videos for new users without prior interaction history (hint: you can use user mood here).

## 🛠️ Specific Tasks

### 1. Data Preprocessing
   - Use the APIs provided to retrieve and preprocess video metadata and user interaction data.
   - Handle missing values, normalize data, and create derived features as needed for the recommendation model.

### 2. Algorithm Development
   - Develop a recommendation algorithm using approaches such as:
     - **Content-based filtering:** Recommending videos similar to those the user has viewed or liked.
     - **Collaborative filtering:** Leveraging similar user preferences to enhance recommendations.
     - **Hybrid models:** Combining content-based and collaborative filtering for improved accuracy.
   - Justify the model selection and describe how it meets the project goals.

### 3. Evaluation Metrics
   - Implement metrics to measure recommendation quality, such as:
     - **Mean Absolute Error (MAE):**
     - **Root Mean Square Error (RMSE):**
   - Summarize results and insights gained from metric evaluations.

### 4. Documentation
   - Provide clear, step-by-step documentation of the approach, model architecture, and key decisions made during development.
   - Craete 3 API endpoint where I am going to give you `username`, `category_id` and `mood`
   - endpoint should be like (In single API call routes will return 10 posts whcih are recomended for user)
   - `http://localhost:port_no/feed?username=your_username&category_id=category_id_user_want_to_see&mood=user_current_mood
   - `http://localhost:port_no/feed?username=your_username&category_id=category_id_user_want_to_see
   - `http://localhost:port_no/feed?username=your_username
