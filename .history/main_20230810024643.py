# app/main.py

from fastapi import FastAPI
from app.api.endpoints.balances import router as balances_router
from app.api.endpoints.history import router as history_router

app = FastAPI()

app.include_router(balances_router, prefix="/balances", tags=["balances"])
app.include_router(history_router, prefix="/history", tags=["history"])
