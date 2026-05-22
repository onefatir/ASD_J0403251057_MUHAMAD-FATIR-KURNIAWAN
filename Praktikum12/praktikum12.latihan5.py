# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Praktikum 12 - Graph II: Shortest Path
# ============================================================

# ==========================================================
# Latihan 5: Studi Kasus Jalur Terpendek Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq
# Graph berbobot hubungan antar kota
# Bobot menunjukkan jarak antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
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

hasil = dijkstra(graph, 'Bogor')
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)

# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# Node awal yang digunakan adalah Bogor.
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# Node yang memiliki jarak paling kecil dari Bogor (selain Bogor itu sendiri) adalah Depok
# dengan jarak 2.
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# Node yang memiliki jarak paling besar dari Bogor adalah Bandung dengan jarak 8
# melalui jalur Bogor -> Depok -> Bandung.
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma Dijkstra bekerja dengan menginisialisasi jarak semua node sebagai tak hingga,
# kecuali node awal (Bogor) yang diberi jarak 0. Kemudian algoritma menggunakan priority
# queue untuk selalu memilih node dengan jarak terkecil yang belum diproses. Dari node
# tersebut, jarak ke setiap tetangganya dihitung dan diperbarui jika ditemukan jalur yang
# lebih pendek. Pada kasus ini, jalur Bogor -> Jakarta secara langsung berjarak 5, namun
# melalui Depok (2 + 2 = 4) lebih pendek sehingga nilainya diperbarui menjadi 4. Begitu
# pula untuk Bandung, jalur melalui Depok (2 + 6 = 8) lebih pendek dibandingkan melalui
# Jakarta (4 + 7 = 11), sehingga jarak terpendek ke Bandung adalah 8.
