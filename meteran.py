import cv2
import pytesseract
import requests
from datetime import datetime
from db import ambil_semua_user
import os
from dotenv import load_dotenv

# Load token & web url dari file .env
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEB_URL = os.getenv('WEB_URL')

def kirim_ke_telegram(pesan):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    daftar_user = ambil_semua_user()

    for chat_id in daftar_user:
        data = {'chat_id': chat_id, 'text': pesan}
        try:
            requests.post(url, data=data)
            print(f"[INFO] Berhasil kirim ke {chat_id}")
        except Exception as e:
            print(f"[ERROR] Gagal kirim ke {chat_id}: {e}")

def kirim_ke_web(angka):
    url = f'{WEB_URL}/update'
    data = {'angka': angka, 'waktu': datetime.now().strftime('%Y-%m-%d %H:%M')}
    requests.post(url, json=data)

def proses_gambar(path_gambar):
    img = cv2.imread(path_gambar)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    hasil_ocr = pytesseract.image_to_string(thresh, config='--psm 7')
    return hasil_ocr.strip()

if __name__ == '__main__':
    hasil = proses_gambar('meteran.jpg')
    waktu = datetime.now().strftime('%d %B %Y, %H:%M')
    pesan = f'Hasil OCR: {hasil}\nWaktu: {waktu}'

    kirim_ke_telegram(pesan)
    kirim_ke_web(hasil)
    print("Pesan berhasil dikirim ke Telegram dan Web.")
