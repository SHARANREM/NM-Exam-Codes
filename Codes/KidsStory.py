from groq import Groq
from textwrap import fill

# ==============================
# CONFIG
# ==============================
API_KEY = "Your_API_Key"
MODEL = "llama-3.3-70b-versatile"

client = Groq(api_key=API_KEY)

# ==============================
# FUNCTIONS
# ==============================
def format_story(story, width=80):
    paragraphs = story.split("\n")
    formatted = "\n\n".join([fill(p, width=width) for p in paragraphs])
    return formatted

def generate_story(prompt):
    system_prompt = (
        "You are a creative storyteller for kids. "
        "Write a fun, imaginative, and simple story suitable for children. "
        "Use easy words, short sentences, and include a moral at the end."
    )

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Create a kids story about: {prompt}"}
        ],
        temperature=0.8,
        max_tokens=800
    )

    story = response.choices[0].message.content.strip()
    return format_story(story)

