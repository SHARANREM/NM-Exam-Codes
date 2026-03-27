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

    return format_output(response.choices[0].message.content.strip())

