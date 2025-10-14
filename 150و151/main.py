from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler,filters

TOKEN = '8352744644:AAHZKvwAg5MnDf7T-4vTedTUMbWTlAaC63o'


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')
#
#
# app = ApplicationBuilder().token(TOKEN).build()
#
# app.add_handler(CommandHandler("hello", hello))
#
# app.run_polling()



async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('iran')


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()