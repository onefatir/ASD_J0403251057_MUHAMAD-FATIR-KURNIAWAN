# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Pertemuan 13 - Latihan 3 - Implementasi Sederhana Algoritma Prim
# ======================

import heapq
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []

    # Menambahkan semua edge yang terhubung dengan node awal ke dalam heap
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    # Menggunakan heap untuk memilih edge dengan bobot terkecil
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
        mst.append((u, v, weight))
        total_weight += weight

        # Menambahkan semua edge yang terhubung dengan node v ke dalam heap
        for neighbor, w in graph[v].items():
            if neighbor not in visited:
                heapq.heappush(edges, (w, v, neighbor))
        

    return mst, total_weight

mst, total = prim(graph, 'A')
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# Pertanyaan Analisis:
# 1. Node awal apa yang digunakan?
# 2. Edge mana yang dipilih pertama kali?
# 3. Bagaimana Prim menentukan edge berikutnya?
# 4. Berapa total bobot MST yang dihasilkan?
# 5. Apa perbedaan pendekatan Prim dan Kruskal?

# Jawaban:
# 1. Node awal yang digunakan adalah 'A'.
# 2. Edge yang dipilih pertama kali adalah (A, C) dengan bobot 2.
# 3. Prim menentukan edge berikutnya dengan memilih edge dengan bobot terkecil yang terhubung dengan node yang sudah dikunjungi.
# 4. Total bobot MST yang dihasilkan adalah 6 (2 + 1 + 3).
# 5. Perbedaan pendekatan Prim dan Kruskal adalah Prim membangun MST dengan memulai dari satu node dan menambahkan 
#    edge dengan bobot terkecil yang terhubung dengan node yang sudah dikunjungi sampai semua node terhubung, sedangkan
#    Kruskal membangun MST dengan mengurutkan semua edge berdasarkan bobot dan menambahkan edge dengan bobot terkecil
#    yang tidak membentuk cycle sampai semua node terhubung.