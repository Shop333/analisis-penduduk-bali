import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Gunakan gaya visual yang lebih modern
plt.style.use('seaborn-v0_8-darkgrid')

# 1. Baca Data
df = pd.read_csv('penduduk_bali.csv')

# 2. Analisis
total_bali = df['Populasi'].sum()
rata_rata = df['Populasi'].mean()
jembrana_data = df[df['Kabupaten'] == 'Jembrana'].iloc[0]

# 3. Setup Plot
fig, ax = plt.subplots(figsize=(14, 8))

# Warna: Jembrana (Orange mencolok), Lainnya (Abu-abu biru agar Jembrana stand out)
colors = ['#FF8C00' if kab == 'Jembrana' else '#A9CCE3' for kab in df['Kabupaten']]

bars = ax.bar(df['Kabupaten'], df['Populasi'], color=colors, edgecolor='white', linewidth=0.7)

# 4. Tambahkan Label Angka di Atas Bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:,}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),  # 5 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold')

# 5. Garis Rata-rata & Anotasi Jembrana
plt.axhline(rata_rata, color='#E74C3C', linestyle='--', alpha=0.6, label=f'Rata-rata: {rata_rata:,.0f}')

# Tambahkan panah penunjuk untuk Jembrana
ax.annotate('Daerah Fokus', 
            xy=('Jembrana', jembrana_data['Populasi']),
            xytext=(0.5, jembrana_data['Populasi'] + 150000),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
            fontsize=11, fontweight='bold', color='#FF8C00')

# 6. Judul dan Label
plt.title('Analisis Demografi Bali: Fokus Wilayah Jembrana', fontsize=20, fontweight='bold', pad=30)
plt.ylabel('Jumlah Populasi (Jiwa)', fontsize=12)
plt.xlabel('Kabupaten / Kota', fontsize=12)
plt.legend(frameon=True, facecolor='white')

# Tambahkan info ringkasan di sudut gambar
info_text = f"Total Populasi Bali: {total_bali:,} jiwa\nUpdate: 2026"
plt.text(0.95, 0.02, info_text, transform=ax.transAxes, fontsize=10,
         verticalalignment='bottom', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

plt.tight_layout()
plt.savefig('analisis_jembrana_premium.png', dpi=300)
print("\n[SUKSES] Grafik 'analisis_jembrana_premium.png' siap")
