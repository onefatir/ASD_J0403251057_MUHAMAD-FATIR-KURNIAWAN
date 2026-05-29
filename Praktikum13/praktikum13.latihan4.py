# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Pertemuan 13 - Latihan 4 - Studi Kasus: Jaringan Kabel Antar Gedung
# ============================================================

# Representasi weighted graph: (bobot, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge berdasarkan bobot terkecil (algoritma Kruskal)
edges.sort()

mst = []
total_biaya = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_biaya += weight
        connected.add(u)
        connected.add(v)

print("Jaringan Kabel Antar Gedung (MST):")
for edge in mst:
    print(edge)
print("Total biaya minimum =", total_biaya)

# Pertanyaan Analisis:
# 1. Algoritma apa yang digunakan?
# 2. Edge mana saja yang dipilih?
# 3. Berapa total biaya minimum?
# 4. Mengapa MST cocok digunakan pada kasus ini?

# Jawaban:
# 1. Algoritma yang digunakan adalah algoritma Kruskal, yaitu dengan mengurutkan edge berdasarkan bobot terkecil
#    lalu memilih edge yang tidak membentuk cycle sampai semua gedung terhubung.
# 2. Edge yang dipilih adalah (GedungC, GedungD) bobot 1, (GedungA, GedungC) bobot 2, dan (GedungB, GedungD) bobot 3.
# 3. Total biaya minimum yang dihasilkan adalah 6 (1 + 2 + 3).
# 4. MST cocok digunakan pada kasus ini karena tujuannya adalah menghubungkan semua gedung dengan total biaya
#    pemasangan kabel paling minimum tanpa adanya hubungan yang berlebih (cycle), sehingga setiap gedung tetap
#    saling terhubung namun biaya yang dikeluarkan seefisien mungkin.
