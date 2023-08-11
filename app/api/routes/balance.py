from fastapi import APIRouter, Depends
from blockchain import get_balance
from mongodb import save_balance_data, get_history
from app.api.models.history import HistoryResponse
from typing import List

router = APIRouter()

@router.get("/balance/{wallet}", response_model=HistoryResponse)
async def fetch_balance(wallet: str, history: List[HistoryResponse] = Depends(get_history)):
    balance_data = get_balance(wallet)
    await save_balance_data(balance_data)
    history.append(HistoryResponse(**balance_data))
    return balance_data
