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
# HEALTH TIPS GENERATOR
# ==============================
def generate_health_tips(scenario, age_group, goal):
    system_prompt = (
        "You are a helpful wellness assistant. "
        "Provide safe, general health tips only. "
        "Do NOT give medical diagnoses or prescribe medications. "
        "Keep advice simple, practical, and easy to follow."
    )

    user_prompt = f"""
    Scenario: {scenario}
    Age Group: {age_group}
    Goal: {goal}

    Provide 6–8 practical health tips.
    Include a short disclaimer at the end.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )

    return response.choices[0].message.content.strip()

# ==============================
# CLI INTERFACE
# ==============================
def main():
    print("\n💪 AI Health Tips Generator 💪\n")

    scenario = input("🩺 Describe your situation (e.g., tired, stressed, poor sleep): ")
    age_group = input("👤 Age Group (child / teen / adult / senior): ")
    goal = input("🎯 Goal (e.g., better sleep, weight loss, more energy): ")

    print("\n⏳ Generating health tips... Please wait...\n")

    tips = generate_health_tips(scenario, age_group, goal)
    formatted_tips = format_output(tips)

    print_boxed("🧾 HEALTH TIPS")
    print(formatted_tips)

    print("\n" + "🌿" * 20)
    print("   STAY HEALTHY")
    print("🌿" * 20 + "\n")

# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    main()