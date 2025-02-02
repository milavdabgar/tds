from fastapi import FastAPI, Query
from typing import List
import json

app = FastAPI()

# Load student marks data from JSON file
with open('q-vercel-python.json', 'r') as f:
    marks_data = json.load(f)
    STUDENT_MARKS = {student['name']: student['marks'] for student in marks_data}

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
