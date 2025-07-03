from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
from db import init_db, tambah_user, ambil_semua_user

BOT_TOKEN = '7810684120:AAF0P7dq2_BCReDQSYhrntTf6sWM24MfFH8'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    username = update.effective_user.username or "pengguna"
    waktu = datetime.now().strftime('%Y-%m-%d %H:%M')

    tambah_user(str(chat_id), username, waktu)

    await update.message.reply_text(
        f"Halo {username}! Terima kasih telah mendaftar notifikasi pembacaan meteran.\n"
        f"Chat ID Anda: {chat_id}\n"
        f"Anda akan mendapatkan notifikasi otomatis saat data meteran diperbarui."
    )
    print(f"[INFO] Pendaftaran user baru: {chat_id} ({username})")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    daftar = ambil_semua_user()
    for chat_id in daftar:
        try:
            await context.bot.send_message(chat_id=chat_id,text="🔔 Pembacaan meteran terbaru telah tersedia! Silakan buka link dashboard untuk melihat hasilnya.")
        except Exception as e:
            print(f"[ERROR] Gagal kirim ke {chat_id}: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    print("Bot sedang berjalan...")
    app.run_polling()
