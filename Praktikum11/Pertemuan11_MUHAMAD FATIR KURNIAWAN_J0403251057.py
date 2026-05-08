# ============================================================
#  Nama  : Muhamad Fatir Kurniawan
#  NIM   : J0403251057
#  Tugas : Pertemuan 11 - Studi Kasus Peta Kota
# ============================================================
#
#  Studi Kasus: Peta Kota (jaringan jalan antar kota di Jawa Timur)
#
#  Node (Kota)  : Surabaya, Malang, Mojokerto, Sidoarjo, Pasuruan, Probolinggo
#  Edge (Jalan) :
#    Surabaya  -- Sidoarjo
#    Surabaya  -- Mojokerto
#    Sidoarjo  -- Pasuruan
#    Pasuruan  -- Malang
#    Pasuruan  -- Probolinggo
#    Malang    -- Probolinggo
#
# ============================================================

NODES = ["Surabaya", "Malang", "Mojokerto", "Sidoarjo", "Pasuruan", "Probolinggo"]

EDGES = [
    ("Surabaya",  "Sidoarjo"),
    ("Surabaya",  "Mojokerto"),
    ("Sidoarjo",  "Pasuruan"),
    ("Pasuruan",  "Malang"),
    ("Pasuruan",  "Probolinggo"),
    ("Malang",    "Probolinggo"),
]


def buildAdjacencyList(nodes, edges):
    # Inisialisasi graph sebagai dictionary dengan setiap node sebagai key dan list kosong sebagai value
    graph = {node: [] for node in nodes}

    # Isi graph berdasarkan edges
    for u, v in edges:
        # Tambahkan vertex v ke daftar adjacency u dan sebaliknya
        graph[u].append(v)
        graph[v].append(u)
    return graph


def buildAdjacencyMatrix(nodes, edges):
    # Buat indeks untuk setiap node agar bisa mengakses posisi dalam matriks
    index = {node: i for i, node in enumerate(nodes)}
    n = len(nodes) # Jumlah vertex
    matrix = [[0] * n for _ in range(n)] # Inisialisasi matriks adjacency dengan 0

    # Isi matriks adjacency berdasarkan edges
    for u, v in edges:
        i, j = index[u], index[v]
        # Tandai adanya sisi antara u dan v dengan 1 (graf tidak berarah)
        matrix[i][j] = 1
        matrix[j][i] = 1
    return matrix


def printNodes(nodes):
    print("Node (Kota):")
    for node in nodes:
        print(f"  - {node}")


def printEdges(edges):
    print("Edge (Jalan):")
    for u, v in edges:
        print(f"  {u} -- {v}")


def printAdjacencyList(graph):
    print("Adjacency List:")
    for node, neighbors in graph.items():
        print(f"  {node}: {neighbors}")


def printAdjacencyMatrix(nodes, matrix):
    print("Adjacency Matrix:")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()


if __name__ == "__main__":
    # Bangun adjacency list dan adjacency matrix dari nodes dan edges
    adjList   = buildAdjacencyList(NODES, EDGES)
    adjMatrix = buildAdjacencyMatrix(NODES, EDGES)

    # Cetak informasi tentang nodes, edges, adjacency list, dan adjacency matrix
    printNodes(NODES)
    print()
    printEdges(EDGES)
    print()
    printAdjacencyList(adjList)
    print()
    printAdjacencyMatrix(NODES, adjMatrix)
