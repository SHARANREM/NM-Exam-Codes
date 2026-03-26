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
# MOVIE RECOMMENDATION GENERATOR
# ==============================
def recommend_movies(mood, genre, language, era):
    system_prompt = (
        "You are a movie recommendation expert. "
        "Suggest engaging and popular movies based on user preferences. "
        "Keep it concise and interesting."
    )

    user_prompt = f"""
    Mood: {mood}
    Genre: {genre}
    Language: {language}
    Era: {era}

    Recommend 6 movies.
    For each movie include:
    - Title
    - Short one-line description
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.8,
        max_tokens=400
    )

    return response.choices[0].message.content.strip()

# ==============================
# CLI INTERFACE
# ==============================
def main():
    print("\n🎬 AI Movie Recommendation System 🎬\n")

    mood = input("😊 Mood (happy / sad / thrilling / chill): ")
    genre = input("🎭 Genre (action / comedy / sci-fi / romance): ")
    language = input("🌐 Language (English / Tamil / Hindi / etc): ")
    era = input("📅 Era (latest / 2010s / classic): ")

    print("\n⏳ Finding perfect movies for you...\n")

    movies = recommend_movies(mood, genre, language, era)
    formatted_movies = format_output(movies)

    print_boxed("🍿 MOVIE RECOMMENDATIONS")
    print(formatted_movies)

    print("\n" + "🎥" * 20)
    print("   ENJOY YOUR MOVIE TIME")
    print("🎥" * 20 + "\n")

# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    main()