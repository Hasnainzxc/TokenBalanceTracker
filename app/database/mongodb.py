from app.settings import MONGODB_URI
from motor.motor_asyncio import AsyncIOMotorClient
from app.api.models.history import HistoryResponse

client = AsyncIOMotorClient(MONGODB_URI)
db = client["token_balance"]
collection = db["balances"]


