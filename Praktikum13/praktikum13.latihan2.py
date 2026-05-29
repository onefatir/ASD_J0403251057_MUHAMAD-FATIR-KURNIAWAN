# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Pertemuan 13 - Latihan 2 - Implementasi Sederhana Algoritma Kruskal
# ============================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)

# Pertanyaan Analisis:
# 1. Edge mana yang dipilih pertama kali?
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# 3. Berapa total bobot MST yang dihasilkan?
# 4. Mengapa edge tertentu tidak dipilih?

# Jawaban:
# 1. Edge yang dipilih pertama kali adalah (C, D) dengan bobot 1.
# 2. Edge dengan bobot paling kecil dipilih lebih dahulu karena algoritma Kruskal bertujuan untuk meminimalkan total bobot MST.
# 3. Total bobot MST yang dihasilkan adalah 6 (1 + 2 + 3).
# 4. Edge tertentu tidak dipilih karena akan membentuk cycle sederhana jika dipilih, 
#    seperti edge (A, D) dengan bobot 5 yang tidak dipilih karena sudah ada edge (C, D) dan (A, C) yang menghubungkan node A dan D.