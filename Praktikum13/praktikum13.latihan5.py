# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Pertemuan 13 - Latihan 5 - Tugas Mandiri: MST Jaringan Jalan Antar Kota
# ============================================================

# Representasi weighted graph: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil (algoritma Kruskal)
edges.sort()

# Inisialisasi MST dan total bobot
mst = []
total_bobot = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_bobot += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree Jaringan Jalan Antar Kota:")
for edge in mst:
    print(edge)
print("Total bobot minimum =", total_bobot)

# Pertanyaan Analisis:
# 1. Kasus apa yang dipilih?
# 2. Algoritma apa yang digunakan?
# 3. Edge mana saja yang dipilih dalam MST?
# 4. Berapa total bobot MST?
# 5. Mengapa edge tertentu tidak dipilih?

# Jawaban:
# 1. Kasus yang dipilih adalah Kasus 1, yaitu Jaringan Jalan Antar Kota (Bogor, Jakarta, Depok, Bandung).
# 2. Algoritma yang digunakan adalah algoritma Kruskal, dengan mengurutkan edge berdasarkan bobot terkecil
#    lalu memilih edge yang tidak membentuk cycle sampai semua kota terhubung.
# 3. Edge yang dipilih dalam MST adalah (Bogor, Depok) bobot 2, (Depok, Jakarta) bobot 3, dan (Depok, Bandung) bobot 4.
# 4. Total bobot MST yang dihasilkan adalah 9 (2 + 3 + 4).
# 5. Edge tertentu tidak dipilih karena akan membentuk cycle jika ditambahkan, seperti edge (Bogor, Jakarta) bobot 5
#    dan (Jakarta, Bandung) bobot 6 yang tidak dipilih karena kota-kota tersebut sudah terhubung melalui edge
#    dengan bobot yang lebih kecil.
