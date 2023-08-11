from app.settings import MONGODB_URI
from motor.motor_asyncio import AsyncIOMotorClient
from app.api.models.history import HistoryResponse

client = AsyncIOMotorClient(MONGODB_URI)
db = client["token_balance"]
collection = db["balances"]

async def save_balance_data(data):
    await collection.insert_one(data)

async def get_history(wallet: str):
    history = await collection.find({"wallet": wallet}).to_list(length=100)
    return [HistoryResponse(**entry) for entry in history]


