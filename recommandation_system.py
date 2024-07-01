import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
ratings = {
    'user1': {'item1': 4, 'item2': 5, 'item3': 1},
    'user2': {'item1': 3, 'item4': 2, 'item5': 5},
    'user3': {'item2': 2, 'item5': 3, 'item6': 4},
    'user4': {'item3': 5, 'item4': 4, 'item6': 2},
    'user5': {'item1': 2, 'item3': 3, 'item5': 4}
}

def calculate_similarity(ratings):
    users = list(ratings.keys())
    num_users = len(users)
    similarity_matrix = np.zeros((num_users, num_users))
    for i in range(num_users):
        for j in range(num_users):
            if i == j:
                similarity_matrix[i, j] = 1  
            else:
                items_i = set(ratings[users[i]].keys())
                items_j = set(ratings[users[j]].keys())
                common_items = list(items_i.intersection(items_j))
                
                if common_items:
                    ratings_i = [ratings[users[i]][item] for item in common_items]
                    ratings_j = [ratings[users[j]][item] for item in common_items]
                    similarity_matrix[i, j] = cosine_similarity([ratings_i], [ratings_j])[0][0]
                else:
                    similarity_matrix[i, j] = 0  
    return similarity_matrix

def recommend_items(user, ratings, similarity_matrix, num_recommendations=3):
    users = list(ratings.keys())
    user_index = users.index(user)
    similar_users = np.argsort(similarity_matrix[user_index])[::-1][1:num_recommendations+1]
    
    recommended_items = {}
    for user_idx in similar_users:
        for item, rating in ratings[users[user_idx]].items():
            if item not in ratings[user] and item not in recommended_items:
                recommended_items[item] = rating
    
    recommended_items = sorted(recommended_items.items(), key=lambda x: x[1], reverse=True)[:num_recommendations]
    return recommended_items

def main():
    similarity_matrix = calculate_similarity(ratings)
    print("Similarity Matrix:")
    print(similarity_matrix)
    
    target_user = 'user1'
    recommendations = recommend_items(target_user, ratings, similarity_matrix)
    print(f"\nRecommendations for {target_user}:")
    for item, score in recommendations:
        print(f"Item: {item}, Score: {score}")

if __name__ == "__main__":
    main()
