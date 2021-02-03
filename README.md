# BBB
BigPump Buying Bot
A small bot to execute a buy order on the $Coin sent on Big Pump Signal's Telegram channel

# REQUIERMENTS   
You need to have Python installed with the following modules:

pyfiglet  
telethon  
python-binance  


To install a module:
```pip install MODULENAME```

# HOW TO USE
Fill the following fields in main.py:   
  -api_id = YOUR TELEGRAM ID  
  -api_hash = 'YOUR TELEGRAM HASH'  
  -phone = 'YOUR PHONE NUMBER (+123456789)' 
Fill the following fields in order_maker.py:   
  -     client = Client("YOUR BINANCE API KEY", "YOUR BINANCE SECRET KEY")
# Aknoledgments
  - This bot trade ONLY USDT pairs
  - This bot retrieve the coin only if it's sent in the following format $coinname
  - You need to create both a Telegram and a Binance API

Feel free to modify this code.
