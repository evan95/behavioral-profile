from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from modules.questionnaire import QUESTIONS, ANIMALS
from modules.personality import ANIMAL_DESCRIPTIONS, ANIMAL_RECOMMENDATIONS, ANIMAL_STRENGTHS_WEAKNESSES, map_option_to_vector

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request, 'questions': QUESTIONS, 'animals': ANIMALS})

@app.post('/result', response_class=HTMLResponse)
async def result(request: Request, answers: str = Form(...)):
    # answers comes as JSON list of selected indexes per question (1–6)
    selections = json.loads(answers)

    # initialize total counters
    totals = {a: 0 for a in ANIMALS}

    # count occurrences of each selected animal
    for choice_idx in selections:
        print(choice_idx)
        animal = map_option_to_vector(choice_idx)
        if animal:
            totals[animal] += 1

    # compute percentages
    s = sum(totals.values())
    percents = {a: round((totals[a] / s) * 100, 1) if s > 0 else 0 for a in ANIMALS}

    # determine top personality
    sorted_animals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    top = sorted_animals[0][0] if sorted_animals else None

    return templates.TemplateResponse(
        'result.html',
        {
            'request': request,
            'totals': totals,
            'percents': percents,
            'top': top,
            'descriptions': ANIMAL_DESCRIPTIONS,
            'recommendations': ANIMAL_RECOMMENDATIONS,
            'strengths_weaknesses': ANIMAL_STRENGTHS_WEAKNESSES,
            'animals': ANIMALS
        }
    )

