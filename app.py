from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Data hasil OCR terakhir
data_terakhir = {"angka": "--", "waktu": "--", "gambar": ""}

@app.route('/')
def index():
    return render_template('index.html', data=data_terakhir)

@app.route('/update', methods=['POST'])
def update_data():
    global data_terakhir
    json_data = request.json
    data_terakhir["angka"] = json_data.get("angka", "--")
    data_terakhir["waktu"] = json_data.get("waktu", datetime.now().strftime('%Y-%m-%d %H:%M'))
    data_terakhir["gambar"] = json_data.get("gambar", "")
    print(f"[INFO] Data diperbarui: {data_terakhir}")
    return jsonify({"status": "success", "data": data_terakhir})

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_terakhir)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=10000)
