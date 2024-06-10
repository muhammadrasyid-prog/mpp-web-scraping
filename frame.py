import pandas as pd
import re

# Membaca file CSV hasil scraping
df_csv = pd.read_csv('hasil_scraping.csv')

# Mengambil angka sebelum kata "gol" dari kolom "Nama Pemain"
df_csv['Total Gol'] = df_csv['Nama Pemain'].apply(lambda x: re.search(r'(\d+)\s*gol', x).group(1) if re.search(r'(\d+)\s*gol', x) else None)

# Mengatur kolom 'Nama Pemain' untuk hanya menampilkan nama pemain dan klub
df_csv['Nama Pemain'] = df_csv['Nama Pemain'].apply(lambda x: re.sub(r'\d+\s*gol:\s*', '', x))

# Mengonversi kolom 'Total Gol' menjadi integer untuk perbandingan
df_csv['Total Gol'] = df_csv['Total Gol'].astype(int)

# Mengambil data pemain dengan gol terbanyak di setiap liga
top_scorers = df_csv.loc[df_csv.groupby('Liga')['Total Gol'].idxmax()]

# Menampilkan DataFrame pemain dengan gol terbanyak di setiap liga
print(top_scorers)
