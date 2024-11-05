import pickle
from flask import Flask, request, jsonify
import pandas as pd
from sentence_transformers import SentenceTransformer
from PIL import Image
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    # You can return some basic info or test functionality
    return {
        "message": "Welcome to the Myntra Swipes API!",
        "available_endpoints": {
            "swipe": "POST /swipe - Submit an image for swiping"
        }
    }

# Load the KMeans model
with open('kmeans.pkl', 'rb') as f:
    kmeans = pickle.load(f)

# Load the CLIP model
model = SentenceTransformer("clip-ViT-B-32")

# Load your dataset
df = pd.read_csv("/workspaces/myntra-swipes/myntra-swipes-demo/backend/outfits.csv")

# Store user preferences
user_preferences = {"yes": [], "no": []}

def generate_image_embedding(image_link):
    """Generate embedding for a single image."""
    try:
        img = Image.open(image_link)
        img_emb = model.encode(img)
        return img_emb
    except Exception as e:
        print(f"Error processing {image_link}: {e}")
        return None

def recommend_similar_items(new_image_embedding):
    """Use the KMeans model to find the cluster and recommend similar items."""
    if new_image_embedding is not None:
        cluster = kmeans.predict([new_image_embedding])[0]
        recommended_items = df[kmeans.labels_ == cluster]['image_link'].tolist()
        return recommended_items
    return []

@app.route('/swipe', methods=['POST'])
def swipe():
    data = request.json
    image_link = data['image_link']
    response = data['response']

    # Update user preferences
    if response == "yes":
        user_preferences["yes"].append(image_link)
    else:
        user_preferences["no"].append(image_link)

    # Generate embedding for the new image
    new_image_embedding = generate_image_embedding(image_link)
    print(f"New Image Embedding: {new_image_embedding}")

    # Gather recommendations based on the new image
    recommended_items = recommend_similar_items(new_image_embedding)
    print(f"Recommended Items Before Exclusion: {recommended_items}")

    # Exclude items swiped "no"
    for item in user_preferences["no"]:
        if item in recommended_items:
            recommended_items.remove(item)

    print(f"Recommended Items After Exclusion: {recommended_items}")
    return jsonify(recommended_items)
