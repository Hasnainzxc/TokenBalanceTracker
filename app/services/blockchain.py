import datetime
from web3 import Web3
from app.settings import ETHEREUM_NODE_URL
import requests
from decouple import config
web3 = Web3(Web3.HTTPProvider(ETHEREUM_NODE_URL))

TOKEN_CONTRACT_ADDRESS = "0xD533a949740bb3306d119CC777fa900bA034cd52"
ABI = [
    {
        "constant": False,
        "inputs": [...],  # Replace with actual input parameters
        "name": "joinPonzi",
        "outputs": [...],  # Replace with actual output parameters
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [...],  # Replace with actual input parameters
        "name": "buyOwnerRole",
        "outputs": [...],  # Replace with actual output parameters
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    # ... other functions ...
]

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
TOKEN_ID = "ethereum"

def get_balance(wallet: str):
    address = web3.to_checksum_address(wallet)
    
    balance = web3.eth.getBalance(address)
    token_contract = web3.eth.contract(address=TOKEN_CONTRACT_ADDRESS, abi=ABI)
    token_balance = token_contract.functions.balanceOf(address).call()

    response = requests.get(f"{COINGECKO_API_URL}/simple/price?ids={TOKEN_ID}&vs_currencies=usd")
    usd_price = response.json()[TOKEN_ID]["usd"]
    
    token_balance_usd = token_balance / 10 ** 18 * usd_price
    
    timestamp = datetime.now().isoformat()
    
    return {
        "wallet": address,
        "timestamp": timestamp,
        "balance": balance,
        "token_balance": token_balance,
        "token_balance_usd": token_balance_usd
    }
