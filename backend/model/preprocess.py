import re

def preprocess_url(url):
    # Feature engineering for the URL
    features = [
        len(url),  # Length of URL
        url.count('.'),  # Number of dots
        url.count('-'),  # Number of hyphens
        url.count('/'),  # Number of slashes
        url.count('@'),  # Number of @ symbols
        1 if 'https' in url else 0,  # Uses HTTPS
        1 if re.search(r'\d', url) else 0,  # Contains digits
    ]
    return features