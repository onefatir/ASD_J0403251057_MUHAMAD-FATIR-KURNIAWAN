# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Pertemuan 13 - Latihan 1
# ============================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")

for edge in edges:
    print(edge)

print("\nSpanning Tree:")

for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Pertanyaan Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

# Jawaban:
# 1. Graph awal memiliki semua edge yang menghubungkan node, sedangkan spanning tree hanya memiliki subset edge yang menghubungkan semua node tanpa membentuk cycle.
# 2. Spanning tree tidak boleh memiliki cycle karena akan melanggar sifat dasar tree yang harus terhubung dan tidak memiliki loop.
# 3. Jumlah edge spanning tree selalu lebih sedikit karena spanning tree hanya membutuhkan (n-1) edge untuk menghubungkan n node, sedangkan graph awal bisa memiliki lebih banyak edge.