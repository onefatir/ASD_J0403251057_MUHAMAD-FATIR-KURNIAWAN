# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Praktikum Pertemuan 11 [1] - Graph Matrix Adjacency Representations
# ============================================================

# Studi Kasus: Peta Kota (jaringan jalan antar kota di Jawa Barat)
def createGraph(V, edges):
    # Inisialisasi matriks adjacency dengan 0
    mat = [[0 for _ in range(V)] for _ in range(V)]
    
    # Isi matriks adjacency berdasarkan edges
    for it in edges:
        u = it[0]
        v = it[1]
        # Tandai adanya sisi antara u dan v dengan 1
        mat[u][v] = 1

        # Jika graf tidak berarah, tambahkan juga sisi sebaliknya
        mat[v][u] = 1

    return mat

if __name__ == "__main__":
    # Jumlah vertex
    V = 4
    
    # Daftar edges (sisi) dalam bentuk pasangan vertex
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]

    # Buat matriks adjacency dari edges
    mat = createGraph(V, edges)
    
    print("Adjacency Matrix:")

    # Cetak matriks adjacency
    for i in range(V):
        for j in range(V):
            print(mat[i][j], end=" ")
        print()