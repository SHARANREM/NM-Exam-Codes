import os
from groq import Groq
from textwrap import fill

# ==============================
# CONFIGURATION
# ==============================
API_KEY = "" # ⚠️ Keep this private
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

def format_poem(poem, width=80):
    # Keep line breaks (important for poems)
    lines = poem.split("\n")
    formatted = "\n".join([fill(line, width=width) for line in lines])
    return formatted

# ==============================
# POEM GENERATOR
# ==============================
def generate_poem(topic, style, mood, length):
    system_prompt = (
        "You are a creative poet. "
        "Write beautiful, expressive poems with vivid imagery and emotion."
    )

    user_prompt = f"""
    Topic: {topic}
    Style: {style} (e.g., rhyming, free verse, haiku)
    Mood: {mood} (e.g., happy, sad, inspirational)
    Length: {length} (short, medium, long)

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

    return response.choices[0].message.content.strip()

# ==============================
# CLI INTERFACE
# ==============================
def main():
    print("\n✨ AI Poem Generator ✨\n")

    topic = input("📝 Enter Poem Topic: ")
    style = input("🎭 Style (rhyming / free verse / haiku): ")
    mood = input("💫 Mood (happy / sad / inspirational): ")
    length = input("📏 Length (short / medium / long): ")

    print("\n⏳ Generating poem... Please wait...\n")

    poem = generate_poem(topic, style, mood, length)
    formatted_poem = format_poem(poem)

    print_boxed("🪶 YOUR POEM")
    print(formatted_poem)

    print("\n" + "🌸" * 20)
    print("   END OF POEM")
    print("🌸" * 20 + "\n")

# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    main()