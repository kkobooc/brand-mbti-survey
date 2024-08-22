from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Static files 경로 설정
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="frontend/templates")

# 질문 리스트
questions = [
    "변화, 개선",
    "애정, 아름다움, 행복, 따스함",
    "행동, 도움, 행위, 움직임",
    "성찰, 탐색, 탐구, 탐험",
    "1인칭, 나 자신, 나에 대한, 내면, 성찰, 스스로",
    "너와 나, 우리, 교류, 교감, 균형",
    "극대화, 최대화, 확산, 모든 이들을 위한, 확대, 확산"
]

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit/", response_class=HTMLResponse)
async def submit_survey(
    request: Request,
    answer1: int = Form(...),
    answer2: int = Form(...),
    answer3: int = Form(...),
    answer4: int = Form(...),
    answer5: int = Form(...),
    answer6: int = Form(...),
    answer7: int = Form(...)
):
    total_score = sum([answer1, answer2, answer3, answer4, answer5, answer6, answer7])
    return templates.TemplateResponse("index.html", {"request": request, "total_score": total_score})
