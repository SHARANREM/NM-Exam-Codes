import gradio as gr

# ==============================
# UI FUNCTION
# ==============================
def app_fn(scenario, age_group, goal):
    if not scenario.strip():
        return "⚠️ Please describe your situation!"
    
    return generate_health_tips(scenario, age_group, goal)

# ==============================
# UI LAYOUT
# ==============================
with gr.Blocks() as app:
    gr.Markdown("# 💪 AI Health Tips Generator")
    gr.Markdown("Get simple and practical health tips 🌿")

    scenario = gr.Textbox(
        label="🩺 Your Situation",
        placeholder="e.g. tired, stressed, poor sleep"
    )

    age_group = gr.Dropdown(
        choices=["Child", "Teen", "Adult", "Senior"],
        label="👤 Age Group"
    )

    goal = gr.Textbox(
        label="🎯 Your Goal",
        placeholder="e.g. better sleep, weight loss, more energy"
    )

    generate_btn = gr.Button("Get Health Tips 🌿")

    output = gr.Textbox(label="🧾 Health Tips", lines=12)

    generate_btn.click(
        fn=app_fn,
        inputs=[scenario, age_group, goal],
        outputs=output
    )

app.launch()