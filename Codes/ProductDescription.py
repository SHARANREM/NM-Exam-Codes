from groq import Groq
from textwrap import fill

# ==============================
# CONFIG
# ==============================
API_KEY = "Your_API_key"
MODEL = "llama-3.3-70b-versatile"

client = Groq(api_key=API_KEY)

# ==============================
# FUNCTIONS
# ==============================
def format_output(text, width=80):
    lines = text.split("\n")
    formatted = "\n".join([fill(line, width=width) for line in lines])
    return formatted

def generate_product_description(name, category, features, audience, tone, price_range):
    system_prompt = (
        "You are an expert e-commerce copywriter. "
        "Write compelling, clear, and engaging product descriptions. "
        "Highlight benefits, not just features. Use persuasive language."
    )

    user_prompt = f"""
    Product Name: {name}
    Category: {category}
    Key Features: {features}
    Target Audience: {audience}
    Tone: {tone}
    Price Range: {price_range}

    Create:
    1. A catchy product title
    2. A short description (2–3 lines)
    3. Key features in bullet points
    4. A persuasive closing line
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.85,
        max_tokens=500
    )

    return format_output(response.choices[0].message.content.strip())

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