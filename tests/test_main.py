from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_fetch_balance():
    response = client.get("/api/v1/balance/0xYOUR_WALLET_ADDRESS")
    assert response.status_code == 200
    data = response.json()
    assert "wallet" in data
    assert "timestamp" in data
    assert "balance" in data
    assert "token_balance" in data
    assert "token_balance_usd" in data
