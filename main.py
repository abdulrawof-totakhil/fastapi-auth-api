from fastapi import FastAPI
from auth import router as auth_router

app = FastAPI(title="FastAPI JWT Auth API")

app.include_router(auth_router, prefix="/auth")

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI JWT Auth API"}
