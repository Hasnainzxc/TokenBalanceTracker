from fastapi import APIRouter, Depends
from app.api.models.history import HistoryResponse
from app.database.mongodb import get_history

router = APIRouter()

@router.get("/history/")
async def get_history_endpoint(wallet: str):
    history = get_history(wallet)
    return [HistoryResponse(**entry) for entry in history]
