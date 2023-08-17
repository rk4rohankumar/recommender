    [model.predict(user_id, item_id).est for item_id in user_items]
    top_items = sorted(zip(user_items, predictions), key=lambda x: x[1], reverse=True)[:n]
    
    return top_items

# Matrix Factorization Recommendations
def get_matrix_factorization_recommendations(user_factors, product_factors, user_id, n=10):
    # Generate matrix factorization recommendations
    user_vector = user_factors[user_id]
    scores = np.dot(user_vector, product_factors)
    top_items = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:n]
    
    return top_items
