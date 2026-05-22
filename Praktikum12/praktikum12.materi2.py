# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Pertemuan 12 - Implementasi Bellman-Ford
# ============================================================

# Representasi graf sebagai adjacency list dengan bobot
graph = {
 'A': {'B': 4, 'C': 2},
 'B': {'D': 5},
 'C': {'D': 1},
 'D': {}
}

def bellman_ford(graph, start):
    # Inisialisasi jarak
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Relaksasi berulang
    for _ in range(len(graph) - 1):
        # Periksa setiap edge
        for node in graph:
            # Periksa semua tetangga
            for neighbor, weight in graph[node].items():
                # Jika ditemukan jarak lebih kecil
                if distances[node] + weight < distances[neighbor]:
                    # Update jarak
                    distances[neighbor] = distances[node] + weight
    
    return distances

# Jalankan algoritma Bellman-Ford dari node 'A'
hasil = bellman_ford(graph, 'A')
print(hasil)