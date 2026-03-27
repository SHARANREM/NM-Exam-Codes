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
def format_poem(poem, width=80):
    # Preserve poem structure (line breaks)
    lines = poem.split("\n")
    formatted = "\n".join([fill(line, width=width) for line in lines])
    return formatted

def generate_poem(topic, style, mood, length):
    system_prompt = (
        "You are a creative poet. "
        "Write beautiful, expressive poems with vivid imagery and emotion."
    )

    user_prompt = f"""
    Topic: {topic}
    Style: {style}
    Mood: {mood}
    Length: {length}

    Write a poem based on the above.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.9,
        max_tokens=500
    )

    return format_poem(response.choices[0].message.content.strip())