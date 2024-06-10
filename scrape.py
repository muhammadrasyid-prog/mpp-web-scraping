import requests
from bs4 import BeautifulSoup
import csv

# Mengambil konten halaman web
url = "https://fajar.co.id/2024/02/19/persaingan-top-skor-5-liga-top-eropa-harry-kane-haaland-bellingham-martinze-dan-mbappa-memimpin/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Mencari elemen yang mengandung informasi liga dan Nama Pemain
ligas_and_top_scorers = soup.find_all('p')

# List untuk menyimpan data liga dan Nama Pemain
data = []

# Variabel untuk menyimpan nama liga
league_name = None

# Menyimpan informasi liga dan Nama Pemain yang diambil
for item in ligas_and_top_scorers:
    if "gol:" in item.text:  # Jika teks mengandung "gol:", itu adalah baris skor pemain
        data.append({"Liga": league_name, "Nama Pemain": item.text})
    elif item.find('strong'):  # Jika memiliki elemen <strong>, itu mungkin adalah nama liga
        league_name = item.find('strong').text

# Menyimpan data ke dalam file CSV
with open('hasil_scraping.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Liga', 'Nama Pemain']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for item in data:
        writer.writerow(item)

print("Data telah disimpan ke dalam file hasil_scraping.csv")
