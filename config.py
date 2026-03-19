# config.py

import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data directory
DATA_PATH = os.path.join(BASE_DIR, "data")

# Index file path
INDEX_FILE = os.path.join(BASE_DIR, "indexing", "index.json")

# Stopwords file (optional for later)
STOPWORDS_FILE = os.path.join(BASE_DIR, "utils", "stopwords.txt")

# Supported file types
SUPPORTED_FORMATS = [".txt"]

# Debug mode
DEBUG = True