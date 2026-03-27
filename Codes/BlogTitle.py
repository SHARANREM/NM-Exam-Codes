from groq import Groq
from textwrap import fill

# ==============================
# CONFIG
# ==============================
API_KEY = "YOUR_API_KEY"
MODEL = "llama-3.3-70b-versatile"

client = Groq(api_key=API_KEY)

# ==============================
# FUNCTIONS
# ==============================
def format_output(text, width=80):
    lines = text.split("\n")
    formatted = "\n".join([fill(line, width=width) for line in lines])
    return formatted

def generate_titles(topic, audience, tone, keywords):
    system_prompt = (
        "You are an expert blog title generator. "
        "Create catchy, SEO-friendly, and engaging blog titles. "
        "Keep them concise and appealing."
    )

    user_prompt = f"""
    Topic: {topic}
    Target Audience: {audience}
    Tone: {tone}
    Keywords: {keywords}

    Generate 8 unique blog titles.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.9,
        max_tokens=300
    )

    return format_output(response.choices[0].message.content.strip())
