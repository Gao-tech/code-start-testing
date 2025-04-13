# app.py
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/python")
async def root():
    return {"message": "Start Serverless Python"}

handler = Mangum(app)