
https://colab.research.google.com/drive/1VYW9TXIpL2CM_ImnJQp9GCwFPNtd-Kkx#scrollTo=WNAVWTBEdBox

https://cee822409b42eabf11.gradio.live/

# 🎵 Smart AI Song Recommendation System
    Using Word Embedding

## 📌 Project Overview

The **Smart AI Song Recommendation System** is a Natural Language Processing (NLP) project that recommends similar songs based on the semantic meaning of song lyrics.

Instead of recommending songs using genres or popularity, this system understands the meaning of lyrics using **Word2Vec Word Embeddings** and finds similar songs using **Cosine Similarity**.

The application provides an interactive **Gradio Web Interface**, allowing users to search for a song and receive the **Top 5 most similar song recommendations** instantly.

---

# 🎯 Problem Statement

Traditional music recommendation systems often rely on artist names, genres, popularity, or user listening history. These approaches may fail to recommend songs that share similar lyrical meaning or emotions.

This project aims to build an AI-powered recommendation system that analyzes song lyrics using **Word Embedding (Word2Vec)** and recommends semantically similar songs using **Cosine Similarity**.

---

# 💡 Solution

The proposed system uses **Natural Language Processing (NLP)** techniques to understand the semantic meaning of song lyrics.

The workflow is as follows:

1. Load the song lyrics dataset.
2. Clean and preprocess the lyrics.
3. Train a Word2Vec model on the lyrics.
4. Generate word embeddings.
5. Create a song embedding by averaging all word vectors.
6. Compute cosine similarity between songs.
7. Recommend the Top 5 most similar songs.
8. Display recommendations using a Gradio web interface.

---

# 🚀 Features

- 🎵 AI-powered song recommendation
- 🔍 Partial song search
- 🔠 Case-insensitive search
- 🧠 Word2Vec word embeddings
- 📈 Cosine Similarity
- 🎧 Interactive Gradio interface
- ⭐ Top 5 similar song recommendations
- ⚡ Fast recommendation system

---

# 🧠 Technologies Used

- Python
- Natural Language Processing (NLP)
- Word2Vec
- Gensim
- Scikit-learn
- Pandas
- NumPy
- Gradio

---

# 📂 Project Workflow

```
Song Lyrics Dataset
        │
        ▼
Text Preprocessing
        │
        ▼
Word2Vec Training
        │
        ▼
Word Embeddings
        │
        ▼
Song Embeddings
        │
        ▼
Cosine Similarity
        │
        ▼
Top 5 Similar Songs
        │
        ▼
Gradio Web Application
```

---

# 📊 Machine Learning Workflow

```
Dataset
   │
   ▼
Preprocessing
   │
   ▼
Tokenization
   │
   ▼
Word2Vec
   │
   ▼
Song Embeddings
   │
   ▼
Cosine Similarity
   │
   ▼
Recommendation Engine
```

---

# 📁 Project Structure

```
Smart-AI-Song-Recommendation-System/

│── app.py
│── songs_dataframe.pkl
│── song_embeddings.pkl
│── requirements.txt
│── README.md
```

---

# ▶️ How to Run the Project

### Step 1

Install the required libraries.

```bash
pip install -r requirements.txt
```

---

### Step 2

Run the application.

```bash
python app.py
```

or

```bash
gradio app.py
```

---

### Step 3

Open the generated Gradio link in your browser.

---

# 🖥️ Application Interface

The Gradio application provides:

- Search box
- Song selection
- Song recommendation
- Top 5 similar songs
- Similarity percentage

---

# 📈 Algorithm Used

### Word2Vec

Word2Vec converts words into dense numerical vectors that capture semantic relationships between words.

---

### Cosine Similarity

Cosine Similarity measures how similar two song embeddings are by comparing the angle between their vectors.

---

# 📊 Output

Input

```
love
```

↓

Output

```
Top 5 Similar Songs

Love Story
Love Yourself
Love Me Do
L.O.V.E.
Baby Girl
```

---

# 🎯 Advantages

- Semantic song recommendation
- Better than keyword matching
- Understands lyric meaning
- Easy to use
- Fast recommendation
- Interactive UI

---

# 📌 Applications

- Music Streaming Platforms
- AI Music Assistants
- Playlist Generation
- Smart Music Search
- Entertainment Recommendation Systems


# 👨‍💻 Prepared by

**R. Sugumar, M.B.A.,**

