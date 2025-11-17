# Example: Stock and Crypto Price Alert Script

import time
import requests
import yfinance as yf

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return data['Close'].iloc[-1]

def get_crypto_price(coin_id):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {'ids': coin_id, 'vs_currencies': 'usd'}
    r = requests.get(url, params=params)
    return r.json()[coin_id]['usd']

def alert_if_needed(asset_name, current_price, threshold):
    if current_price >= threshold:
        print(f"ALERT: {asset_name} price ${current_price} is above threshold ${threshold}.")
    else:
        print(f"{asset_name} price ${current_price} is below threshold ${threshold}.")

# Example usage:
ASSET = "bitcoin"  # or "AAPL" for stock
IS_CRYPTO = True
THRESHOLD = 50000

while True:
    if IS_CRYPTO:
        price = get_crypto_price(ASSET)
        alert_if_needed("Bitcoin", price, THRESHOLD)
    else:
        price = get_stock_price(ASSET)
        alert_if_needed("Apple Inc.", price, THRESHOLD)
    time.sleep(5)  # Check every 60 seconds