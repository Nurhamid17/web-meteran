import sqlite3

def init_db():
    conn = sqlite3.connect('pengguna.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user (
        chat_id TEXT PRIMARY KEY,
        username TEXT,
        waktu TEXT
    )''')
    conn.commit()
    conn.close()

def tambah_user(chat_id, username, waktu):
    conn = sqlite3.connect('pengguna.db')
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO user VALUES (?, ?, ?)", (chat_id, username, waktu))
    conn.commit()
    conn.close()

def ambil_semua_user():
    conn = sqlite3.connect('pengguna.db')
    c = conn.cursor()
    c.execute("SELECT chat_id FROM user")
    results = [row[0] for row in c.fetchall()]
    conn.close()
    return results

# Panggil init_db sekali di awal
init_db()
