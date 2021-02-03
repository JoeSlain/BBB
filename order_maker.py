from binance.client import Client

def place_order(coin, amount):
    #symbz=coin.upper()+'USDT'
    #print(symbz)
    client = Client("YOUR BINANCE API KEY", "YOUR BINANCE SECRET KEY")
    order = client.create_test_order(
    symbol=coin.upper()+'USDT',
    side=Client.SIDE_BUY,
    type=Client.ORDER_TYPE_MARKET,
    quantity=amount)
