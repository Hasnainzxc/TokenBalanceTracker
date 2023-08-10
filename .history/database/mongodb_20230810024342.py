# app/database/mongodb.py

from pymongo import MongoClient
from app.settings import settings

client = MongoClient(settings.mongo_db_url)
db = client["token_balance"]
balances_collection = db["balances"]
