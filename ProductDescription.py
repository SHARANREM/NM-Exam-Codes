import os
from groq import Groq
from textwrap import fill

# ==============================
# CONFIGURATION
# ==============================
API_KEY = ""  # ⚠️ Keep this private
MODEL = "llama-3.3-70b-versatile"

# ==============================
# INITIALIZE CLIENT
# ==============================
client = Groq(api_key=API_KEY)

# ==============================
# HELPER FUNCTION FOR CLEAN OUTPUT
# ==============================
def print_boxed(text, width=80):
    print("\n" + "═" * width)
    for line in text.split("\n"):
        print("║ " + line.ljust(width - 4) + " ║")
    print("═" * width + "\n")

def format_output(text, width=80):
    lines = text.split("\n")
    formatted = "\n".join([fill(line, width=width) for line in lines])
    return formatted

# ==============================
# PRODUCT DESCRIPTION GENERATOR
# ==============================
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

    return response.choices[0].message.content.strip()

# ==============================
# CLI INTERFACE
# ==============================
def main():
    print("\n🛍️ AI Product Description Generator 🛍️\n")

    name = input("📦 Product Name: ")
    category = input("🏷️ Category: ")
    features = input("⚙️ Key Features (comma separated): ")
    audience = input("🎯 Target Audience: ")
    tone = input("🎨 Tone (professional / luxury / fun / minimal): ")
    price_range = input("💰 Price Range (budget / mid / premium): ")

    print("\n⏳ Generating product description... Please wait...\n")

    description = generate_product_description(
        name, category, features, audience, tone, price_range
    )

    formatted_description = format_output(description)

    print_boxed("📝 PRODUCT DESCRIPTION")
    print(formatted_description)

    print("\n" + "🚀" * 20)
    print("   READY TO SELL")
    print("🚀" * 20 + "\n")

# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    main()