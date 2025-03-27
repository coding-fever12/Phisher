# Phishing Detector ML Model

A machine learning model for detecting phishing attempts in emails and URLs.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Prepare your data:
- Place your training data in `data/data.csv`
- The CSV should have columns: domain, subdomain, label

4. Train the model:
```bash
python train_model.py
```

5. Run the API:
```bash
python run.py
```

## API Endpoints

### POST /predict
Predict if an email or URL is phishing.

Request body:
```json
{
    "type": "email",  // or "url"
    "content": "email content here"  // for email type
    // or
    "url": "https://example.com"  // for url type
}
```

Response:
```json
{
    "is_phishing": true/false,
    "probability": 0.95,
    "confidence": 0.9
}
```

### GET /health
Check API health status.

Response:
```json
{
    "status": "healthy",
    "model_loaded": true/false
}
```

## Model Features

### Email Features
- Content length
- Number of @ symbols
- Number of URLs
- Number of suspicious words
- Number of exclamation marks

### URL Features
- URL length
- Number of dots
- Number of hyphens
- Number of slashes
- Number of special characters
- HTTPS presence
- www presence

## Development

### Project Structure
```
ml-model/
├── app/
│   ├── models/      # Saved model files
│   ├── __init__.py  # Flask app initialization
│   ├── routes.py    # API endpoints
│   └── utils.py     # Utility functions
├── data/            # Training data
├── config.py        # Configuration
├── data_preprocessing.py  # Data preprocessing
├── train_model.py   # Model training
├── run.py          # API server
└── requirements.txt # Dependencies
```

### Training Data Format
The training data should be in CSV format with the following columns:
- domain: The domain name
- subdomain: The subdomain information
- label: Binary label (0 for legitimate, 1 for phishing)

## License
MIT License