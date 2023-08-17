# Matrix Factorization for Personalized Ranking

# Retrieve user interaction data from SQLite database
def retrieve_user_interaction_data():
    # Set up SQLite connection
    conn = sqlite3.connect('user_interactions.db')
    
    # Read data from SQLite into DataFrame
    df = pd.read_sql_query('SELECT * FROM user_interactions', conn)
    
    # Close connection
    conn.close()
    
    return df

# Create user-product interaction matrix
def create_user_product_matrix(df):
    # Create user-product interaction matrix
    matrix = df.pivot(index='user_id', columns='product_id', values='rating')
    
    return matrix

# Preprocess user-product interaction matrix
def preprocess_matrix(matrix):
    # Fill missing values with 0
    matrix = matrix.fillna(0)
    
    return matrix

# Perform Non-Negative Matrix Factorization (NMF) using scikit-learn
def perform_matrix_factorization(matrix, n_components):
    # Perform NMF
    model = NMF(n_components=n_components)
    user_factors = model.fit_transform(matrix)
    product_factors = model.components_
    
    return user_factors, product_factors
