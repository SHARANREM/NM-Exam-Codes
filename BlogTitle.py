import os
from groq import Groq
from textwrap import fill

API_KEY = ""  # Replace with your Groq API key
MODEL = "llama-3.3-70b-versatile"
client = Groq(api_key=API_KEY)

def print_boxed(text, width=80):
    print("\n" + "═" * width)
    for line in text.split("\n"):
        print("║ " + line.ljust(width - 4) + " ║")
    print("═" * width + "\n")

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

    return response.choices[0].message.content.strip()

def main():
    print("\n✨ AI Blog Title Generator ✨\n")

    topic = input("📝 Enter Blog Topic: ")
    audience = input("🎯 Target Audience (e.g., students, developers): ")
    tone = input("🎨 Tone (e.g., professional, fun, catchy): ")
    keywords = input("🔑 Keywords (comma separated): ")

    print("\n⏳ Generating titles... Please wait...\n")

    titles = generate_titles(topic, audience, tone, keywords)
    formatted_titles = format_output(titles)

    print_boxed("📰 BLOG TITLE IDEAS")
    print(formatted_titles)

    print("\n" + "🚀" * 20)
    print("   DONE")
    print("🚀" * 20 + "\n")


if __name__ == "__main__":
    main()