from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler,filters
from test import get_avg_price_from_divar
TOKEN = '8352744644:AAHZKvwAg5MnDf7T-4vTedTUMbWTlAaC63o'

async def handele_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip()
    await update.message.reply_text(f"'در حال جستجو برای {query}'...")

    avg= get_avg_price_from_divar(query)
    if avg:
        await update.message.reply_text(f"میانگین قیمت {avg:,}تومان")
    else:
        await update.message.reply_text("نتیجه یافت نشد")
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handele_query))

app.run_polling()