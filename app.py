import gradio as gr
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# ======================================================
# Load Data
# ======================================================

df = pd.read_pickle("songs_dataframe.pkl")

with open("song_embeddings.pkl", "rb") as f:
    song_embeddings = pickle.load(f)

# ======================================================
# Search Song
# ======================================================

def search_song(keyword):

    keyword = str(keyword).strip().lower()

    if keyword == "":
        return gr.update(choices=[], value=None)

    matches = df[
        df["song_name"].str.lower().str.contains(keyword, na=False)
    ].head(100)

    if len(matches) == 0:
        return gr.update(choices=[], value=None)

    songs = (
        matches["song_name"]
        + "  |  "
        + matches["artist"]
    ).tolist()

    return gr.update(
        choices=songs,
        value=songs[0]
    )


# ======================================================
# Recommendation
# ======================================================

def recommend_song(selected_song):

    if not selected_song:
        return "❌ Please search and select a song."

    song_name = selected_song.split("  |  ")[0]

    idx = df[df["song_name"] == song_name].index[0]

    scores = cosine_similarity(
        [song_embeddings[idx]],
        song_embeddings
    )[0]

    similar = scores.argsort()[::-1]

    output = []

    output.append("🎵 SELECTED SONG")
    output.append("-" * 50)
    output.append(f"Song   : {df.iloc[idx]['song_name']}")
    output.append(f"Artist : {df.iloc[idx]['artist']}")
    output.append("")
    output.append("⭐ TOP 5 RECOMMENDED SONGS")
    output.append("-" * 50)
    output.append("")

    count = 1

    for i in similar:

        if i == idx:
            continue

        output.append(f"{count}. {df.iloc[i]['song_name']}")
        output.append(f"   Artist      : {df.iloc[i]['artist']}")
        output.append(f"   Similarity  : {scores[i]:.3f}")
        output.append("")

        count += 1

        if count > 5:
            break

    return "\n".join(output)


# ======================================================
# CSS
# ======================================================

css = """
.gradio-container{
    max-width:950px !important;
    margin:auto;
}

footer{
    visibility:hidden;
}

textarea{
    font-size:15px !important;
}
"""


# ======================================================
# UI
# ======================================================

with gr.Blocks(
    title="Smart AI Song Recommendation System",
    css=css,
    fill_width=True
) as demo:

    gr.Markdown(
        """
# 🎵 Smart AI Song Recommendation System

Recommend similar songs using **Word2Vec** and **Cosine Similarity**.
"""
    )

    with gr.Row():

        with gr.Column(scale=1):

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

            clear_btn = gr.ClearButton(
                [keyword, song_dropdown]
            )

        with gr.Column(scale=2):

            output = gr.Textbox(
                label="Recommendations",
                lines=20,
                interactive=False
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

demo.queue()
demo.launch()
