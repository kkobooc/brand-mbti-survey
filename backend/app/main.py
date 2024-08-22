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
    "당신은 새로운 경험을 즐깁니까?",
    "스트레스를 쉽게 받습니까?",
    "팀워크를 중요하게 생각합니까?",
    "대화를 통해 문제를 해결하려 합니까?",
    "다른 사람의 감정을 잘 이해합니까?",
    "계획을 세우고 이를 따르는 편입니까?",
    "리더십 역할을 맡는 것을 좋아합니까?"
]

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "questions": questions})

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
    return templates.TemplateResponse("index.html", {"request": request, "total_score": total_score, "questions": questions})
