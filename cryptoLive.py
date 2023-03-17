import requests
import json
import time
import telegram

# Replace <YOUR_TELEGRAM_BOT_TOKEN> with your Telegram bot token
bot = telegram.Bot(token='<YOUR_TELEGRAM_BOT_TOKEN>')

# Replace <YOUR_API_KEY> with your CoinMarketCap API key
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=<YOUR_API_KEY>'

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
    time.sleep(60)  # Check again in 60 seconds
