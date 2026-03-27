import gradio as gr

# ==============================
# UI FUNCTION
# ==============================
def app_fn(name, category, features, audience, tone, price_range):
    if not name.strip():
        return "⚠️ Please enter a product name!"
    
    return generate_product_description(
        name, category, features, audience, tone, price_range
    )

# ==============================
# UI LAYOUT
# ==============================
with gr.Blocks() as app:
    gr.Markdown("# 🛍️ AI Product Description Generator")
    gr.Markdown("Create high-converting product descriptions 🚀")

    name = gr.Textbox(label="📦 Product Name")

    category = gr.Textbox(
        label="🏷️ Category",
        placeholder="e.g. Electronics, Fashion"
    )

    features = gr.Textbox(
        label="⚙️ Key Features",
        placeholder="comma separated"
    )

    audience = gr.Textbox(
        label="🎯 Target Audience",
        placeholder="e.g. Students, Professionals"
    )

    tone = gr.Dropdown(
        choices=["Professional", "Luxury", "Fun", "Minimal"],
        label="🎨 Tone"
    )

    price_range = gr.Dropdown(
        choices=["Budget", "Mid", "Premium"],
        label="💰 Price Range"
    )

    generate_btn = gr.Button("Generate Description 🛍️")

    output = gr.Textbox(label="📝 Product Description", lines=15)

    generate_btn.click(
        fn=app_fn,
        inputs=[name, category, features, audience, tone, price_range],
        outputs=output
    )

app.launch()