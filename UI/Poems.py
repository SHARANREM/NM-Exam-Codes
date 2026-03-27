import gradio as gr

# ==============================
# UI FUNCTION
# ==============================
def app_fn(topic, style, mood, length):
    if not topic.strip():
        return "⚠️ Please enter a poem topic!"
    
    return generate_poem(topic, style, mood, length)

# ==============================
# UI LAYOUT
# ==============================
with gr.Blocks() as app:
    gr.Markdown("# ✨ AI Poem Generator")
    gr.Markdown("Create beautiful poems with emotion and style 🪶")

    topic = gr.Textbox(
        label="📝 Topic",
        placeholder="e.g. Nature, Love, Dreams"
    )

    style = gr.Dropdown(
        choices=["Rhyming", "Free Verse", "Haiku"],
        label="🎭 Style"
    )

    mood = gr.Dropdown(
        choices=["Happy", "Sad", "Inspirational", "Romantic"],
        label="💫 Mood"
    )

    length = gr.Dropdown(
        choices=["Short", "Medium", "Long"],
        label="📏 Length"
    )

    generate_btn = gr.Button("Generate Poem 🪶")

    output = gr.Textbox(label="🪶 Your Poem", lines=15)

    generate_btn.click(
        fn=app_fn,
        inputs=[topic, style, mood, length],
        outputs=output
    )

app.launch()