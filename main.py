from fastapi import FastAPI
from auth.main import router

app = FastAPI()
app.include_router(router)  # signup/login only