import telebot
import requests
TOKEN = '8352744644:AAHZKvwAg5MnDf7T-4vTedTUMbWTlAaC63o'
bot = telebot.TeleBot(TOKEN)
URL="https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
@bot.message_handler(commands=['start','help','hello'])
def send_welcome(message):
    # print(message.text)
    bot.reply_to(message,"hi im samoraii what can i do for you")

@bot.message_handler(func=lambda m: True)
def show_price(message):
    symbol=message.text.upper()
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    if response.status_code == 200:
        data = response.json()
        # print(data)
        # bot.reply_to(message,'hello')
        bot.reply_to(message ,f"{data['symbol']} price is {data['price']}")
    else:
        bot.reply_to(message,"some is wrong...")

bot.infinity_polling()