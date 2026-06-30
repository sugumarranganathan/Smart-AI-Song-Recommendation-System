https://colab.research.google.com/drive/1VYW9TXIpL2CM_ImnJQp9GCwFPNtd-Kkx#scrollTo=WNAVWTBEdBox

https://sugumarranganathan-smart-ai-song-recommendation-system.hf.space

# 🎵 Smart AI Song Recommendation System

## 📖 Project Overview

The **Smart AI Song Recommendation System** is an intelligent music recommendation application that helps users discover songs similar to their favorite tracks. Instead of manually searching through thousands of songs, users can simply search for a song, select it, and instantly receive the **Top 5 similar song recommendations**. The application makes music discovery faster, easier, and more enjoyable through an interactive and user-friendly interface.

---

# 🎯 Problem Statement

With **millions of songs** available, choosing the **right music** has become more challenging than ever. Users often miss **great songs** because they do not know what to search for next. This project helps users **find songs related to the music they already enjoy**. It provides **instant recommendations**, reduces the **effort of manual searching**, and makes discovering **new music** more convenient. The system offers a **better listening experience** and encourages users to **explore more songs**. It is suitable for **music streaming platforms**, **entertainment services**, and **digital music libraries** that want to improve **user satisfaction**.

---

# 💡 Solution

The Smart AI Song Recommendation System allows users to search for their favorite songs using a simple keyword search. After selecting a song, the application instantly displays the **Top 5 recommended songs** along with the **artist name** and **similarity score**. The recommendation process is fast, user-friendly, and helps users discover new music without manually browsing large collections. This solution improves the overall music listening experience and encourages users to explore songs related to their interests.

---

# 🚀 Features

- 🔍 Search songs using keywords
- 🎵 Select songs from matching search results
- ⭐ Recommend Top 5 similar songs
- 👤 Display artist name
- 📊 Display similarity score
- ⚡ Fast recommendation using precomputed embeddings
- 💻 Interactive Gradio web interface
- 🌐 Deployable on Hugging Face Spaces

---

# 🧠 Word Embedding Workflow

```text
                    Song Lyrics Dataset
                            │
                            ▼
                     Text Cleaning
          (Lowercase, Remove Symbols,
          Punctuation & Extra Spaces)
                            │
                            ▼
                      Tokenization
              (Split Lyrics into Words)
                            │
                            ▼
                 Remove Stop Words
                            │
                            ▼
              Train Word2Vec Model
                    (Skip-Gram)
                            │
                            ▼
                 Generate Word Vectors
                            │
                            ▼
               Create Song Embeddings
            (Average of Word Vectors)
                            │
                            ▼
        Save Dataset & Embeddings (.pkl)
```

---

# 🔄 Project Processing Workflow

```text
                      Start
                        │
                        ▼
         Load Song Dataset (.pkl)
                        │
                        ▼
      Load Song Embeddings (.pkl)
                        │
                        ▼
        User Searches a Song
                        │
                        ▼
      Find Matching Songs
                        │
                        ▼
      User Selects a Song
                        │
                        ▼
 Retrieve Selected Song Embedding
                        │
                        ▼
  Calculate Cosine Similarity
                        │
                        ▼
     Rank Similar Songs
                        │
                        ▼
 Display Top 5 Recommendations
 (Song • Artist • Similarity Score)
                        │
                        ▼
                       End
```

---

# 📋 Project Workflow

| Step | Description |
|------|-------------|
| 1 | Load the preprocessed song dataset. |
| 2 | Load the precomputed song embeddings. |
| 3 | User enters a song keyword. |
| 4 | The application searches for matching songs. |
| 5 | Matching songs are displayed in a dropdown. |
| 6 | User selects one song. |
| 7 | Retrieve the embedding of the selected song. |
| 8 | Calculate similarity with all available songs. |
| 9 | Rank songs based on similarity score. |
| 10 | Display the Top 5 recommended songs. |

---

# 🛠️ Technologies Used

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| User Interface | Gradio |
| Data Processing | Pandas, NumPy |
| NLP | Word2Vec |
| Machine Learning | Cosine Similarity |
| Model Storage | Pickle |

---

# 📂 Project Structure


Smart-AI-Song-Recommendation-System/
│
├── app.py
├── songs_dataframe.pkl
├── song_embeddings.pkl
├── requirements.txt
├── README.md


# 📸 Application Screenshots

### 🔍 Search Song

Users can search for songs using a keyword and select the desired song from the matching results.

### 🎵 Recommendation Result

The application displays the selected song along with the **Top 5 recommended songs**, including the artist name and similarity score.


# 📊 Applications

- Music Streaming Platforms
- Entertainment Applications
- Online Music Libraries
- Personalized Music Recommendation Systems
- Digital Music Services

---

# 👨‍💻 Prepared by

**Sugumar Ranganathan**

