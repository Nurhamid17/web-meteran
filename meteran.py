import cv2
import pytesseract
import requests
from datetime import datetime

# Konfigurasi Bot Telegram
BOT_TOKEN = '7810684120:AAF0P7dq2_BCReDQSYhrntTf6sWM24MfFH8'
CHAT_ID = '6669229070'

def kirim_ke_telegram(pesan):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': pesan}
    requests.post(url, data=data)

def kirim_ke_web(angka):
    url = url = 'https://web-meteran.onrender.com/update' 
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
