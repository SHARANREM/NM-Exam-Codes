import os
from groq import Groq
from textwrap import fill

# ==============================
# CONFIGURATION
# ==============================
API_KEY = ""  # Replace with your Groq API key
MODEL = "llama-3.3-70b-versatile" # You can change model if needed

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

def format_story(story, width=80):
    paragraphs = story.split("\n")
    formatted = "\n\n".join([fill(p, width=width) for p in paragraphs])
    return formatted

# ==============================
# MAIN FUNCTION
# ==============================
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

    return response.choices[0].message.content.strip()

# ==============================
# CLI INTERFACE
# ==============================
def main():
    print("\n✨ Welcome to AI Kids Story Generator ✨")
    print("Type your idea and watch the magic happen!\n")

    user_input = input("🧸 Enter your story idea: ")

    print("\n⏳ Generating story... Please wait...\n")

    story = generate_story(user_input)
    formatted_story = format_story(story)

    print_boxed("📖 YOUR STORY")
    print(formatted_story)

    print("\n" + "🌟" * 20)
    print("   THE END")
    print("🌟" * 20 + "\n")

# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    main()