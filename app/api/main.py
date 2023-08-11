from fastapi import FastAPI
from app.api.routes import balance

app = FastAPI()

app.include_router(balance.router, prefix="/api/v1")
