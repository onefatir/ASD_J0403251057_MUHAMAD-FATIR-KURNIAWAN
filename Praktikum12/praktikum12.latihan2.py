# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Praktikum 12 - Graph II: Shortest Path
# ============================================================

# ==========================================================
# Latihan 2: Implementasi Algoritma Dijkstra
# ==========================================================

import heapq
# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

hasil = dijkstra(graph, 'A')
print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
# Jarak terpendek dari A ke B adalah 4
# 2. Berapa jarak terpendek dari A ke C?
# Jarak terpendek dari A ke C adalah 2
# 3. Berapa jarak terpendek dari A ke D?
# Jarak terpendek dari A ke D adalah 3
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# Karena bobot edge A-C (2) + C-D (1) = 3 lebih kecil daripada bobot edge A-B (4) + B-D (5) = 9
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# Fungsi priority_queue dalam algoritma Dijkstra adalah untuk menyimpan dan mengambil node dengan 
# jarak terpendek secara efisien.
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
# Karena algoritma Dijkstra mengasumsikan semua bobot positif, dan tidak dapat menangani situasi di mana 
# penambahan edge dengan bobot negatif dapat menghasilkan jarak yang lebih pendek.