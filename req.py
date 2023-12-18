import requests
import json

# URL endpoint untuk API
api_url = 'http://localhost:5000/predict'  # Sesuaikan dengan alamat dan port API Anda

# Contoh data teks yang ingin diuji
text_to_predict = "Saya merasa tanda - tanda kecemasan ketika berada di tempat keramaian"

# Membuat payload untuk dikirim ke API
payload = {'text': text_to_predict}
headers = {'Content-Type': 'application/json'}

# Mengirim permintaan POST ke API
response = requests.post(api_url, data=json.dumps(payload), headers=headers)

# Menampilkan respons dari API
if response.status_code == 200:
    results = response.json()
    print("Hasil prediksi:")
    print(json.dumps(results, indent=2))
else:
    print("Gagal menghubungi API. Kode status:", response.status_code)
    print(response.text)
