from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.api.routes import balance
from fastapi.templating import Jinja2Templates

from blockchain import get_balance

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.get("/api/v1/balance")
async def fetch_balance(wallet: str):
    return get_balance(wallet)