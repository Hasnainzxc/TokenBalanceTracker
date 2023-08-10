from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from datetime import datetime
import pymongo
from web3 import Web3
import httpx

app = FastAPI()

# MongoDB configuration
mongo_client = pymongo.MongoClient("mongodb://mongo:27017/")
db = mongo_client["wallet_balances"]
collection = db["balances"]

# Web3 configuration
web3 = Web3(Web3.HTTPProvider("YOUR_ETH_NODE_URL"))

class WalletBalance(BaseModel):
    wallet: str
    balance: float
    balance_usd: float
    timestamp: str

@app.get("/balance/")
async def get_balance(wallet: str):
    address = Web3.toChecksumAddress(wallet)
    balance = web3.eth.getBalance(address) / 10 ** 18

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd")
        eth_price = response.json()["ethereum"]["usd"]

    balance_usd = balance * eth_price

    timestamp = datetime.now().isoformat()

    # Save balance to MongoDB
    collection.insert_one({
        "wallet": wallet,
        "last_update_time": timestamp,
        "current_balance": balance,
        "current_balance_usd": balance_usd,
    })

    return WalletBalance(wallet=wallet, balance=balance, balance_usd=balance_usd, timestamp=timestamp)

@app.get("/history/")
async def get_history(wallet: str):
    # Retrieve history from MongoDB
    history = list(collection.find({"wallet": wallet}))

    return history
