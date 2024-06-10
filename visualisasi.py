import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca file CSV hasil scraping
df_csv = pd.read_csv('hasil_scraping.csv')

# Mengambil angka sebelum kata "gol" dari kolom "Nama Pemain"
df_csv['Total Gol'] = df_csv['Nama Pemain'].apply(lambda x: re.search(r'(\d+)\s*gol', x).group(1) if re.search(r'(\d+)\s*gol', x) else None)

# Mengupdate kolom 'Nama Pemain' untuk hanya menampilkan nama pemain dan klub
df_csv['Nama Pemain'] = df_csv['Nama Pemain'].apply(lambda x: re.sub(r'\d+\s*gol:\s*', '', x))

# Mengonversi kolom 'Total Gol' menjadi integer untuk perbandingan
df_csv['Total Gol'] = df_csv['Total Gol'].astype(int)

# Mengambil data pemain dengan gol terbanyak di setiap liga
top_scorers = df_csv.loc[df_csv.groupby('Liga')['Total Gol'].idxmax()]

# Menambahkan informasi liga ke kolom 'Nama Pemain'
top_scorers['Nama Pemain'] = top_scorers.apply(lambda row: f"{row['Nama Pemain']} ({row['Liga']})", axis=1)

# Membuat visualisasi bar chart
plt.figure(figsize=(14, 8))
sns.barplot(x='Nama Pemain', y='Total Gol', data=top_scorers, palette='viridis')

# Menambahkan judul dan label
plt.title('Top Scorers from the Top 5 Best Leagues in Europe', fontsize=16)
plt.xlabel('Player (Club, League)', fontsize=14)
plt.ylabel('Total Goals', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Menampilkan plot
plt.tight_layout()
plt.show()
