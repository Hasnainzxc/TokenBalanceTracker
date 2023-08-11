from fastapi import APIRouter, Depends
from app.api.models.balance import BalanceResponse
from app.services.blockchain import get_balance

router = APIRouter()

@router.get("/balance/")
async def get_balance_endpoint(wallet: str):
    balance = get_balance(wallet)
    return BalanceResponse(**balance)
