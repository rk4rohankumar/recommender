# Collaborative Filtering using Surprise

# Load data from SQLite database using Surprise's Dataset and Reader classes
def load_data_surprise():
    # Set up SQLite connection
    conn = sqlite3.connect('user_interactions.db')
    
    # Read data from SQLite into DataFrame
    df = pd.read_sql_query('SELECT * FROM user_interactions', conn)
    
    # Define rating scale
    reader = Reader(rating_scale=(1, 5))
    
    # Load dataset
    data = Dataset.load_from_df(df[['user_id', 'product_id', 'rating']], reader)
    
    # Close connection
    conn.close()
    
    return data

# Split data into training and testing sets
def split_data_train_test(data):
    # Split data into training and testing sets
    trainset, testset = train_test_split(data, test_size=0.2, random_state=42)
    
    return trainset, testset

# Train collaborative filtering model using Surprise's SVD algorithm
def train_collaborative_filtering_model(trainset):
    # Train the model using the training set
    model = SVD()
    model.fit(trainset)
    
    return model

# Evaluate model performance using metrics like Mean Squared Error (MSE)
def evaluate_model_performance(model, testset):
    # Evaluate model performance using MSE
    predictions = model.test(testset)
    mse = surprise.accuracy.mse(predictions)
    
    return mse
