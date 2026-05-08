# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Praktikum Pertemuan 11 [3] - Konversi Matrix ke List
# ============================================================

def matrixToList(matrix):
    # Dapatkan jumlah vertex dari ukuran matriks
    V = len(matrix)

    # Inisialisasi adjacency list sebagai dictionary kosong
    adjList = {}

    # Isi adjacency list berdasarkan matriks adjacency
    for i in range(V):
        adjList[i] = []
        for j in range(V):
            # Jika ada sisi antara vertex i dan j (nilai 1), tambahkan j ke daftar adjacency i
            if matrix[i][j] == 1:
                adjList[i].append(j)

    return adjList

if __name__ == "__main__":
    # Contoh matriks adjacency untuk graf dengan 4 vertex
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]

    # Konversi matriks adjacency ke adjacency list
    adjList = matrixToList(matrix)

    # Cetak adjacency list
    print("Adjacency List:")
    for i in adjList:
        print(f"{i}: {adjList[i]}")
