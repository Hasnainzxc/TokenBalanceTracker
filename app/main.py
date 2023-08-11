from fastapi import FastAPI
from app.api.routes import balance, history

app = FastAPI()

app.include_router(balance.router)
app.include_router(history.router)
