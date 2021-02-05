from binance.client import Client
import requests
import json

def place_order(coin, amount):
    client = Client("BINANCE HASH", "SECRET HASH")
    order = client.create_order(
    symbol=coin+'BTC',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity= int(float(amount) / float(json.loads(requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+coin+"BTC").text)["price"])))
    
    price = float(json.loads(requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+coin+"BTC").text)["price"])
    balance = json.loads(client.get_asset_balance(asset=coin)["free"])
    
    order = client.order_limit_sell(
    symbol=coin+'BTC',
    quantity=int(balance),
    price= f"{2*price:.8f}")

