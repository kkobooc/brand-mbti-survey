from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 정적 파일 및 템플릿 설정
app.mount("/static", StaticFiles(directory="./frontend/static"), name="static")
templates = Jinja2Templates(directory="./frontend/templates")

# 루트 페이지 (index.html) 렌더링
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 첫 번째 질문 페이지 GET 요청 처리
@app.get("/question_1", response_class=HTMLResponse)
async def get_question_1(request: Request):
    return templates.TemplateResponse("question_1.html", {"request": request})

# 첫 번째 질문 페이지 POST 요청 처리
@app.post("/question_1", response_class=HTMLResponse)
async def post_question_1(request: Request, response_1: int = Form(...)):
    # 응답 저장 가능 (DB 또는 메모리 등)
    # 다음 질문으로 리다이렉트
    return RedirectResponse(f"/question_2?response_1={response_1}", status_code=303)

# 두 번째 질문 페이지 GET 요청 처리
@app.get("/question_2", response_class=HTMLResponse)
async def get_question_2(request: Request, response_1: int):
    return templates.TemplateResponse("question_2.html", {"request": request, "response_1": response_1})

# 두 번째 질문 페이지 POST 요청 처리
@app.post("/question_2", response_class=HTMLResponse)
async def post_question_2(request: Request, response_1: int = Form(...), response_2: int = Form(...)):
    # 응답 저장 가능 (DB 또는 메모리 등)
    # 다음 질문으로 리다이렉트
    return RedirectResponse(f"/question_3?response_1={response_1}&response_2={response_2}", status_code=303)

# 세 번째 질문 페이지 GET 요청 처리
@app.get("/question_3", response_class=HTMLResponse)
async def get_question_3(request: Request, response_1: int, response_2: int):
    return templates.TemplateResponse("question_3.html", {"request": request, "response_1": response_1, "response_2": response_2})

# 세 번째 질문 페이지 POST 요청 처리
@app.post("/question_3", response_class=HTMLResponse)
async def post_question_3(request: Request, response_1: int = Form(...), response_2: int = Form(...), response_3: int = Form(...)):
    # 응답 저장 가능 (DB 또는 메모리 등)
    # 다음 질문으로 리다이렉트
    return RedirectResponse(f"/question_4?response_1={response_1}&response_2={response_2}&response_3={response_3}", status_code=303)

# 네 번째 질문 페이지 GET 요청 처리
@app.get("/question_4", response_class=HTMLResponse)
async def get_question_4(request: Request, response_1: int, response_2: int, response_3: int):
    return templates.TemplateResponse("question_4.html", {"request": request, "response_1": response_1, "response_2": response_2, "response_3": response_3})

# 네 번째 질문 페이지 POST 요청 처리
@app.post("/question_4", response_class=HTMLResponse)
async def post_question_4(request: Request, response_1: int = Form(...), response_2: int = Form(...), response_3: int = Form(...), response_4: int = Form(...)):
    # 응답 저장 가능 (DB 또는 메모리 등)
    # 다음 질문으로 리다이렉트
    return RedirectResponse(f"/question_5?response_1={response_1}&response_2={response_2}&response_3={response_3}&response_4={response_4}", status_code=303)

# 다섯 번째 질문 페이지 GET 요청 처리
@app.get("/question_5", response_class=HTMLResponse)
async def get_question_5(request: Request, response_1: int, response_2: int, response_3: int, response_4: int):
    return templates.TemplateResponse("question_5.html", {"request": request, "response_1": response_1, "response_2": response_2, "response_3": response_3, "response_4": response_4})

# 다섯 번째 질문 페이지 POST 요청 처리
@app.post("/question_5", response_class=HTMLResponse)
async def post_question_5(request: Request, response_1: int = Form(...), response_2: int = Form(...), response_3: int = Form(...), response_4: int = Form(...), response_5: int = Form(...)):
    # 응답 저장 가능 (DB 또는 메모리 등)
    # 다음 질문으로 리다이렉트
    return RedirectResponse(f"/question_6?response_1={response_1}&response_2={response_2}&response_3={response_3}&response_4={response_4}&response_5={response_5}", status_code=303)

# 여섯 번째 질문 페이지 GET 요청 처리
@app.get("/question_6", response_class=HTMLResponse)
async def get_question_6(request: Request, response_1: int, response_2: int, response_3: int, response_4: int, response_5: int):
    return templates.TemplateResponse("question_6.html", {"request": request, "response_1": response_1, "response_2": response_2, "response_3": response_3, "response_4": response_4, "response_5": response_5})

# 여섯 번째 질문 페이지 POST 요청 처리
@app.post("/question_6", response_class=HTMLResponse)
async def post_question_6(request: Request, response_1: int = Form(...), response_2: int = Form(...), response_3: int = Form(...), response_4: int = Form(...), response_5: int = Form(...), response_6: int = Form(...)):
    # 응답 저장 가능 (DB 또는 메모리 등)
    # 다음 질문으로 리다이렉트
    return RedirectResponse(f"/question_7?response_1={response_1}&response_2={response_2}&response_3={response_3}&response_4={response_4}&response_5={response_5}&response_6={response_6}", status_code=303)

# 일곱 번째 질문 페이지 GET 요청 처리
@app.get("/question_7", response_class=HTMLResponse)
async def get_question_7(request: Request, response_1: int, response_2: int, response_3: int, response_4: int, response_5: int, response_6: int):
    return templates.TemplateResponse("question_7.html", {"request": request, "response_1": response_1, "response_2": response_2, "response_3": response_3, "response_4": response_4, "response_5": response_5, "response_6": response_6})

# 일곱 번째 질문 페이지 POST 요청 처리
@app.post("/question_7", response_class=HTMLResponse)
async def post_question_7(request: Request, response_1: int = Form(...), response_2: int = Form(...), response_3: int = Form(...), response_4: int = Form(...), response_5: int = Form(...), response_6: int = Form(...), response_7: int = Form(...)):
    # 응답 저장 가능 (DB 또는 메모리 등)
    # 연락처 입력 페이지로 리다이렉트
    return RedirectResponse(f"/contact?response_1={response_1}&response_2={response_2}&response_3={response_3}&response_4={response_4}&response_5={response_5}&response_6={response_6}&response_7={response_7}", status_code=303)

# 연락처 입력 페이지 GET 요청 처리
@app.get("/contact", response_class=HTMLResponse)
async def get_contact(request: Request, response_1: int, response_2: int, response_3: int, response_4: int, response_5: int, response_6: int, response_7: int):
    return templates.TemplateResponse("contact.html", {"request": request, "response_1": response_1, "response_2": response_2, "response_3": response_3, "response_4": response_4, "response_5": response_5, "response_6": response_6, "response_7": response_7})

# 연락처 페이지 POST 요청 처리
# @app.post("/contact", response_class=HTMLResponse) # 페이지 반환시
@app.post("/contact")
async def post_contact(
    request: Request,
    phone: str = Form(...),
    email: str = Form(...),
    response_1: int = Form(...),
    response_2: int = Form(...),
    response_3: int = Form(...),
    response_4: int = Form(...),
    response_5: int = Form(...),
    response_6: int = Form(...),
    response_7: int = Form(...)
        ):
    # 설문 응답을 리스트로 저장
    responses = {
        "response_1": response_1,
        "response_2": response_2,
        "response_3": response_3,
        "response_4": response_4,
        "response_5": response_5,
        "response_6": response_6,
        "response_7": response_7
    }
    # 유형 목록
    categories = [
        {"no": 1, "a": "response_1", "b": "response_5", "type": "magician"},
        {"no": 2, "a": "response_1", "b": "response_6", "type": "hero"},
        {"no": 3, "a": "response_1", "b": "response_7", "type": "outlaw"},
        {"no": 4, "a": "response_2", "b": "response_5", "type": "lover"},
        {"no": 5, "a": "response_2", "b": "response_6", "type": "jester"},
        {"no": 6, "a": "response_2", "b": "response_7", "type": "every man"},
        {"no": 7, "a": "response_3", "b": "response_5", "type": "creator"},
        {"no": 8, "a": "response_3", "b": "response_6", "type": "caregiver"},
        {"no": 9, "a": "response_3", "b": "response_7", "type": "ruler"},
        {"no": 10, "a": "response_4", "b": "response_5", "type": "innocent"},
        {"no": 11, "a": "response_4", "b": "response_6", "type": "sage"},
        {"no": 12, "a": "response_4", "b": "response_7", "type": "explorer"},
    ]
    
    # C값을 계산하고 가장 높은 유형을 찾는 로직
    max_score = -1
    highest_category = None

    # 모든 카테고리를 돌면서 C(AxB)를 계산
    for category in categories:
        a_value = responses[category["a"]]
        b_value = responses[category["b"]]
        c_value = a_value * b_value  # C(AxB)

        # 최대값을 가진 카테고리 선택, 동점일 경우 No가 높은 것 선택
        if c_value > max_score or (c_value == max_score and category["no"] < highest_category["no"]):
            max_score = c_value
            highest_category = category
    
    return {
        "message": "Survey submitted",
        "phone": phone,
        "email": email,
        "highest_category": highest_category["type"],
        "score": max_score,
        "responses": responses
    }