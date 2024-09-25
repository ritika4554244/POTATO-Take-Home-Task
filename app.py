from flask import Flask, request, jsonify, render_template
import pandas as pd
from flask_caching import Cache 

# Create a Flask application instance
app = Flask(__name__)

# Initialize Cache
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})

# Load the dataset from a TSV file
df = pd.read_csv("Dataset/cleaned.tsv", sep='\t')  # Adjust path as needed
print(df.dtypes)

# Attempt to convert 'created_at' to datetime, specifying utc=True

df['created_at'] = pd.to_datetime(df['created_at'].str.strip(), utc=True)



@app.route('/')
def home():
    return render_template("temps/homes.html")

@app.route('/query', methods=['GET'])

def query_data():
    
    
    term = request.args.get('term')  # Get the query term from the request parameters
    
    if not term:  # Check if the term is provided
        return jsonify({"error": "No search term provided"}), 400

    # Filter the dataset for tweets that contain the search term (case-insensitive)
    filtered_data = df[df['text'].str.contains(term, case=False, na=False)]

    # Check if any tweets were found
    if filtered_data.empty:
        return jsonify({"error": "No tweets found containing the term"}), 404

  
  
    # Group by date and count tweets
    tweets_per_date = filtered_data['created_at'].dt.date.value_counts().sort_index().to_dict()
    tweets_per_hour = filtered_data['created_at'].dt.hour.value_counts().sort_index().to_dict()
        

    result = {
        "How many tweets were posted containing the term on each day?": {str(key): int(value) for key, value in tweets_per_date.items()},
        "How many unique users posted a tweet containing the term?": int(filtered_data['author_id'].nunique()),
        "How many likes did tweets containing the term get, on average?": float(filtered_data['like_count'].mean()) if 'like_count' in filtered_data.columns else 0.0,
        "Where (in terms of place IDs) did the tweets come from?": filtered_data['place_id'].value_counts().to_dict(),
        "What times of day were the tweets posted at?": {str(key): int(value) for key, value in tweets_per_hour.items()},
        "Which user posted the most tweets containing the term?": str(filtered_data['author_id'].value_counts().idxmax())
    }
    
    
    return jsonify(result) # Return the results as a JSON response

if __name__ == '__main__':
    
    app.run(debug=True) # Run the Flask application in debug mode



