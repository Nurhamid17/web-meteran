from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7810684120:AAF0P7dq2_BCReDQSYhrntTf6sWM24MfFH8'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"Halo, Chat ID kamu: {chat_id}")
    print(f"Chat ID baru: {chat_id}")  # Ini untuk log di terminal
    # Nanti bisa simpan chat_id ke file atau database

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    print("Bot sedang berjalan...")
    app.run_polling()
