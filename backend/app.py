from flask import Flask, request, jsonify
from model.predict import predict_phishing
import json

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    # Predict using the AI model
    is_phishing = predict_phishing(url)
    return jsonify({"url": url, "is_phishing": is_phishing})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)