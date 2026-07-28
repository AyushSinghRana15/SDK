"""Simple app for testing dependency updates."""
import requests
import numpy as np
import pandas as pd
from flask import Flask

app = Flask(__name__)

def fetch_users(url):
    """Fetch users from API."""
    response = requests.get(url)
    return response.json()

def process_data(data):
    """Process data with numpy."""
    arr = np.array(data)
    return arr.mean()

def create_dataframe(data):
    """Create pandas dataframe."""
    return pd.DataFrame(data)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
