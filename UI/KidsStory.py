import gradio as gr

# ==============================
# UI FUNCTION
# ==============================
def app_fn(user_input):
    if not user_input.strip():
        return "⚠️ Please enter a story idea!"
    return generate_story(user_input)

# ==============================
# UI
# ==============================
interface = gr.Interface(
    fn=app_fn,
    inputs=gr.Textbox(label="🧸 Enter your story idea"),
    outputs=gr.Textbox(label="📖 Your Story"),
    title="✨ AI Kids Story Generator",
    description="Enter your idea and generate a fun kids story with a moral!"
)

interface.launch()