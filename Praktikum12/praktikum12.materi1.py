# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Pertemuan 12 - Implementasi Djikstra
# ============================================================

import heapq

# Representasi graf sebagai adjacency list dengan bobot
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}

# Implementasi algoritma Dijkstra
def dijkstra(graph, start):
    # Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}
    # Jarak node awal = 0
    distances[start] = 0
    # Priority queue
    pq = [(0, start)]

    # Proses hingga priority queue kosong
    while pq:
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)
        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                # Update jarak dan masukkan ke priority queue
                distances[neighbor] = distance
                # Masukkan ke priority queue dengan jarak baru
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Jalankan algoritma Dijkstra dari node 'A'
hasil = dijkstra(graph, 'A')
print(hasil)
