import gradio as gr

# ==============================
# UI FUNCTION
# ==============================
def app_fn(mood, genre, language, era):
    if not mood.strip():
        return "⚠️ Please select your mood!"
    
    return recommend_movies(mood, genre, language, era)

# ==============================
# UI LAYOUT
# ==============================
with gr.Blocks() as app:
    gr.Markdown("# 🎬 AI Movie Recommendation System")
    gr.Markdown("Find the perfect movie based on your mood 🍿")

    mood = gr.Dropdown(
        choices=["Happy", "Sad", "Thrilling", "Chill"],
        label="😊 Mood"
    )

    genre = gr.Dropdown(
        choices=["Action", "Comedy", "Sci-Fi", "Romance", "Horror", "Drama"],
        label="🎭 Genre"
    )

    language = gr.Textbox(
        label="🌐 Language",
        placeholder="e.g. English, Tamil, Hindi"
    )

    era = gr.Dropdown(
        choices=["Latest", "2010s", "2000s", "Classic"],
        label="📅 Era"
    )

    generate_btn = gr.Button("Recommend Movies 🍿")

    output = gr.Textbox(label="🎥 Movie Recommendations", lines=12)

    generate_btn.click(
        fn=app_fn,
        inputs=[mood, genre, language, era],
        outputs=output
    )

app.launch()