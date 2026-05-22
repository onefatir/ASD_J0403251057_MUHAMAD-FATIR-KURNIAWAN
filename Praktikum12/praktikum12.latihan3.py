# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Praktikum 12 - Graph II: Shortest Path
# ============================================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================
# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
            # Jika jarak ke node saat ini sudah diketahui,
            # dan ditemukan jarak yang lebih kecil ke neighbor,
            # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    return distances

hasil = bellman_ford(graph, 'A')
print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
# Bobot langsung dari A ke B adalah 5
# 2. Berapa total bobot jalur A -> C -> B?
# Total bobot jalur A -> C -> B adalah 4 (A ke C) + (-2) (C ke B) = 2
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# Jalur A -> C -> B menghasilkan jarak lebih kecil menuju B karena memiliki total bobot yang lebih kecil (2 < 5)
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini melakukan relaksasi pada semua edge secara berulang, sehingga dapat menangani perubahan jarak yang disebabkan oleh bobot negatif.
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# Proses relaksasi edge adalah proses di mana algoritma memeriksa apakah jarak ke suatu node melalui edge 
# tertentu lebih kecil daripada jarak yang sudah diketahui sebelumnya. Jika ya, maka jarak 
# tersebut diperbarui dengan nilai yang lebih kecil.
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
# Perbedaan utama antara Bellman-Ford dan Dijkstra adalah bahwa Bellman-Ford dapat menangani graph dengan bobot negatif,
# sedangkan Dijkstra tidak dapat. Selain itu, Bellman-Ford memiliki kompleksitas waktu O(V * E)
# sedangkan Dijkstra memiliki kompleksitas waktu O((V + E) log V) dengan menggunakan priority queue.