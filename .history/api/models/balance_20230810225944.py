from pydantic import BaseModel

class BalanceResponse(BaseModel):
    wallet: str
    timestamp: str
    balance: int
    token_balance: int
    token_balance_usd: float
