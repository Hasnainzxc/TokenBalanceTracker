from fastapi import FastAPI
from app.api.endpoints import balances, history

app = FastAPI()

app.include_router(balances.router)
app.include_router(history.router)
