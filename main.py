import json
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
ANSWER = json.loads(Path(__file__).with_name("answer.json").read_text(encoding="utf-8"))

@app.get("/")
async def get_answer():
    return JSONResponse(content=ANSWER)

@app.get("/answer.json")
async def get_answer_file():
    return JSONResponse(content=ANSWER)
