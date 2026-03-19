# 🔍 Mini Search Engine

A modular, scalable mini search engine built with a system design approach.  
This project demonstrates core concepts like preprocessing, indexing, query handling, and ranking.

---

## 🚀 Features

- Text preprocessing (tokenization, stopword removal, stemming)
- Inverted index for fast search
- Query processing engine
- Ranking system (TF / TF-IDF)
- Modular architecture for scalability

---

## 🏗️ Architecture
Data → Preprocessing → Indexing → Query Engine → Ranking → Results




### 🔹 Offline Phase
- Data cleaning
- Index building

### 🔹 Online Phase
- Query processing
- Fast retrieval using index
- Ranking results



---

## ⚙️ Setup Instructions


---------------------
# Clone repo
git clone search-engine

# Navigate
cd  search-engine

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run project
python main.py



## Dataset Handling

- Documents are loaded from `/data`
- Supported format: `.txt`
- Each document is assigned a unique ID
- Structured format:

{
  id,
  title,
  content,
  path
}