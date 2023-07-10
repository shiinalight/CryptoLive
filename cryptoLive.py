import requests
import json
import time
import telegram

bot = telegram.Bot(token='<MY_TELEGRAM_BOT_TOKEN>')

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='

def get_price():
    response = requests.get(url)
    data = json.loads(response.text)['data']
    prices = ''
    for item in data[:10]:
        name = item['name']
        symbol = item['symbol']
        price = item['quote']['USD']['price']
        prices += f'{name} ({symbol}): {price:.2f} USD\n'
    return prices

while True:
    try:
        prices = get_price()
        bot.send_message(chat_id=<YOUR_CHAT_ID>, text=prices)
    except Exception as e:
        print(str(e))
    time.sleep(60)  
