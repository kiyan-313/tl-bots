import telebot

TOKEN = '8352744644:AAHZKvwAg5MnDf7T-4vTedTUMbWTlAaC63o'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help','hello'])
def send_welcome(message):
    # print(message.text)
    bot.reply_to(message,'hi im samoraii what can i do for you')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text=='salam':
        bot.reply_to(message,'salam azizim')
    else:
        bot.reply_to(message,'chi migi')
    # bot.reply_to(message, 'salam azizim')

bot.infinity_polling()