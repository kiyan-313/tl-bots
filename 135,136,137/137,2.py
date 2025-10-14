import telebot
import requests
from dotenv import load_dotenv
import os

# بارگذاری متغیرهای .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
# بارگذاری متغیرهای .env
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help','hello'])
def send_welcome(message):
    bot.reply_to(message,"hi im samoraii what can i do for you")

@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol = message.text.upper()
    if not symbol.endswith("USDT"):
        symbol += "USDT"

    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    if response.status_code == 200:
        data = response.json()
        bot.reply_to(message, f"{data['symbol']} price is {data['price']}")
    else:
        bot.reply_to(message,"⚠️ some is wrong...")

bot.infinity_polling()