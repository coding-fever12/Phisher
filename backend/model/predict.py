import tensorflow as tf
import numpy as np
from preprocess import preprocess_url

# Load the trained model
model = tf.keras.models.load_model('model.h5')

def predict_phishing(url):
    # Preprocess the URL
    features = preprocess_url(url)
    
    # Predict
    prediction = model.predict(np.array([features]))
    return bool(prediction[0][0] > 0.5)  # Threshold for phishing