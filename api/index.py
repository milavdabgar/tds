from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Student marks data
STUDENT_MARKS = {
    "1": 77,
    "2": 14,
    "3": 81,
    "4": 11,
    "5": 62
}

@app.get("/")
async def root():
    return {"message": "Student Marks API"}

@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    marks = [STUDENT_MARKS.get(n) for n in name]
    return {"marks": marks}

# Add CORS headers
@app.middleware("http")
async def add_cors_headers(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response
