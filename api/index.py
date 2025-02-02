from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the student marks data
df = pd.read_csv('marks.csv')

@app.get("/api")
async def get_marks(name: list[str]):
    # Get marks for the requested names
    marks = [int(df[df['name'] == n]['marks'].iloc[0]) if len(df[df['name'] == n]) > 0 else None for n in name]
    return {"marks": marks}
