import json
from jinja2 import Environment, FileSystemLoader
from modules.questionnaire import QUESTIONS, ANIMALS
from modules.personality import (
    ANIMAL_DESCRIPTIONS,
    ANIMAL_RECOMMENDATIONS,
    ANIMAL_STRENGTHS_WEAKNESSES,
)

import os

# Create output directory
os.makedirs("dist", exist_ok=True)

env = Environment(loader=FileSystemLoader("templates"))

# Render index.html
template = env.get_template("index.html")
html = template.render(
    questions=QUESTIONS,
    animals=ANIMALS
)
with open("dist/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Rendered index.html")

# Optional: If result.html needs static content, render it too
template = env.get_template("result.html")
html = template.render(
    descriptions=ANIMAL_DESCRIPTIONS,
    recommendations=ANIMAL_RECOMMENDATIONS,
    strengths_weaknesses=ANIMAL_STRENGTHS_WEAKNESSES,
    animals=ANIMALS,
    top=None, totals={}, percents={}
)
with open("dist/result.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Rendered result.html")

# Copy static folder
os.system("cp -r static dist/")
