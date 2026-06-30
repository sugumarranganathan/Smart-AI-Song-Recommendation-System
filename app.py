import gradio as gr
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# Load Data
# ==========================================

df = pd.read_pickle("songs_dataframe.pkl")

with open("song_embeddings.pkl", "rb") as f:
    song_embeddings = pickle.load(f)

# ==========================================
# Find Matching Songs
# ==========================================

def search_song(keyword):

    if keyword.strip() == "":
        return gr.update(choices=[], value=None)

    keyword = keyword.lower().strip()

    matches = df[
        df["song_name"].str.lower().str.contains(keyword, na=False)
    ]

    if matches.empty:
        return gr.update(choices=[], value=None)

    song_list = (
        matches["song_name"]
        + "  |  "
        + matches["artist"]
    ).tolist()

    return gr.update(
        choices=song_list,
        value=song_list[0]
    )

# ==========================================
# Recommendation Function
# ==========================================

def recommend_song(selected_song):

    if selected_song is None:
        return "❌ Please search and select a song."

    song_name = selected_song.split(" | ")[0]

    idx = df[df["song_name"] == song_name].index[0]

    similarity_scores = cosine_similarity(
        [song_embeddings[idx]],
        song_embeddings
    )[0]

    similar_indices = similarity_scores.argsort()[::-1]

    result = []

    result.append(f"🎵 Selected Song : {df.iloc[idx]['song_name']}")
    result.append(f"👤 Artist : {df.iloc[idx]['artist']}")
    result.append("")
    result.append("=" * 45)
    result.append("Top 5 Recommended Songs")
    result.append("=" * 45)
    result.append("")

    count = 1

    for i in similar_indices:

        if i == idx:
            continue

        result.append(
            f"{count}. {df.iloc[i]['song_name']}"
        )

        result.append(
            f"   👤 Artist : {df.iloc[i]['artist']}"
        )

        result.append(
            f"   ⭐ Similarity : {similarity_scores[i]:.3f}"
        )

        result.append("")

        count += 1

        if count > 5:
            break

    return "\n".join(result)

# ==========================================
# UI
# ==========================================

with gr.Blocks(title="Smart AI Song Recommendation System") as demo:

    gr.Markdown(
        """
# 🎵 Smart AI Song Recommendation System

### Recommend similar songs using **Word2Vec** and **Cosine Similarity**
        """
    )

    with gr.Row():

        with gr.Column():

            keyword = gr.Textbox(
                label="🔍 Search Song",
                placeholder="Example: love"
            )

            search_btn = gr.Button(
                "🔍 Search",
                variant="primary"
            )

            song_dropdown = gr.Dropdown(
                choices=[],
                label="🎵 Select Song",
                interactive=True
            )

            recommend_btn = gr.Button(
                "🎶 Recommend Songs",
                variant="primary"
            )

        with gr.Column():

            output = gr.Textbox(
                label="Recommendations",
                lines=18
            )

    search_btn.click(
        search_song,
        inputs=keyword,
        outputs=song_dropdown
    )

    recommend_btn.click(
        recommend_song,
        inputs=song_dropdown,
        outputs=output
    )

demo.launch()
