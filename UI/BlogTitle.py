import gradio as gr

# ==============================
# UI FUNCTION
# ==============================
def app_fn(topic, audience, tone, keywords):
    if not topic.strip():
        return "⚠️ Please enter a blog topic!"
    
    return generate_titles(topic, audience, tone, keywords)

# ==============================
# UI LAYOUT
# ==============================
with gr.Blocks() as app:
    gr.Markdown("# ✨ AI Blog Title Generator")
    gr.Markdown("Generate catchy and SEO-friendly blog titles 🚀")

    topic = gr.Textbox(label="📝 Blog Topic", placeholder="e.g. AI in Healthcare")
    audience = gr.Textbox(label="🎯 Target Audience", placeholder="e.g. Students, Developers")
    tone = gr.Textbox(label="🎨 Tone", placeholder="e.g. Professional, Fun, Catchy")
    keywords = gr.Textbox(label="🔑 Keywords", placeholder="comma separated")

    generate_btn = gr.Button("Generate Titles 🚀")

    output = gr.Textbox(label="📰 Blog Title Ideas", lines=10)

    generate_btn.click(
        fn=app_fn,
        inputs=[topic, audience, tone, keywords],
        outputs=output
    )

app.launch()