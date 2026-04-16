import pandas as pd
import matplotlib.pyplot as plt

# 1. Baca Data
df = pd.read_csv('penduduk_bali.csv')

# 2. Analisis Tambahan
total_bali = df['Populasi'].sum()
rata_rata = df['Populasi'].mean()
kab_terkecil = df.loc[df['Populasi'].idxmin()]
kab_terbesar = df.loc[df['Populasi'].idxmax()]

print("\n=== RINGKASAN ANALISIS EKSEKUTIF ===")
print(f"Total Penduduk Bali : {total_bali:,} jiwa")
print(f"Rata-rata per Kab   : {rata_rata:,.0f} jiwa")
print(f"Kabupaten Terkecil  : {kab_terkecil['Kabupaten']} ({kab_terkecil['Populasi']:,} jiwa)")
print(f"Kabupaten Terbesar  : {kab_terbesar['Kabupaten']} ({kab_terbesar['Populasi']:,} jiwa)")

# 3. Visualisasi dengan Highlight Jembrana
plt.figure(figsize=(12, 6))

# Buat daftar warna: Merah untuk Jembrana, Biru untuk yang lain
colors = ['red' if kab == 'Jembrana' else 'skyblue' for kab in df['Kabupaten']]

plt.bar(df['Kabupaten'], df['Populasi'], color=colors)
plt.axhline(rata_rata, color='green', linestyle='--', label='Rata-rata') # Garis rata-rata

plt.title('Perbandingan Populasi Kabupaten di Bali (Highlight Jembrana)', fontsize=14)
plt.ylabel('Jumlah Jiwa')
plt.legend()
plt.xticks(rotation=45)

# Simpan hasil
plt.tight_layout()
plt.savefig('analisis_jembrana.png')
print("\n[BERHASIL] Grafik baru 'analisis_jembrana.png' telah dibuat!")
