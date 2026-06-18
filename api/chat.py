import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Vercel will safely read this key from the environment dashboard configurations
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        
        # Make the request securely from the cloud backend
        response = requests.post(
            ENDPOINT,
            headers={
                "Content-Type": "application/json",
                "x-goog-api-key": GEMINI_API_KEY
            },
            json=data
        )
        
        return jsonify(response.json()), response.status_code
        
    except Exception as e:
        return jsonify({"error": {"message": str(e)}}), 500