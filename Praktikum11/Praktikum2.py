# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Praktikum Pertemuan 11 [2] - Graph Adjacency List Representations
# ============================================================

def createGraph(edges):
    # Inisialisasi graph sebagai dictionary kosong
    graph = {}

    # Isi graph berdasarkan edges
    for u, v in edges:
        # Pastikan setiap vertex memiliki daftar adjacency, jika belum ada buat baru
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        # Tambahkan vertex v ke daftar adjacency u dan sebaliknya
        graph[u].append(v)
        graph[v].append(u)
    return graph

if __name__ == "__main__":
    # Daftar edges (sisi) dalam bentuk pasangan vertex
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]

    # Buat graph adjacency list dari edges
    graph = createGraph(edges)

    print("Adjacency List:")
    # Cetak adjacency list
    for i in graph:
        print(f"{i}: {graph[i]}", end=" ")
        for j in graph[i]:
            print(f"  {j}", end=" ")
        print()
