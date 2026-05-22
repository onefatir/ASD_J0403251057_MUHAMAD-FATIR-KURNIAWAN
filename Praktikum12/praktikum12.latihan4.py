# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Praktikum 12 - Graph II: Shortest Path
# ============================================================

# ==========================================================
# Latihan 3: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra
# ==========================================================

import heapq
# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    # Proses hingga priority queue kosong
    while priority_queue:
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)
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

hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit melalui jalur Gerbang -> Kantin -> Lab -> Aula.
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# Tidak, jalur langsung tidak selalu menghasilkan jarak paling kecil karena bobot (waktu tempuh) dari
# setiap edge berbeda. Dalam kasus ini, meskipun jalur langsung dari Gerbang ke Aula tidak ada, 
# jalur melalui Kantin dan Lab memberikan waktu tempuh yang lebih cepat dibandingkan dengan jalur 
# lain yang mungkin memiliki lebih sedikit edge.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
# Dijkstra cocok digunakan pada kasus lokasi kampus ini karena graf yang digunakan
#  memiliki bobot positif (waktu tempuh), dan algoritma Dijkstra dirancang untuk menemukan jalur
# terpendek dalam graf dengan bobot non-negatif. Selain itu, Dijkstra efisien untuk graf yang tidak terlalu besar, seperti dalam kasus ini.
