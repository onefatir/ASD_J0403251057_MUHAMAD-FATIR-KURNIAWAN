#=======================================================================================
# Nama    : Muhamad Fatir Kurniawan
# NIM     : J0403251057
# Kelas   : A1
#=======================================================================================

#=======================================================================================
# Implementasi Dasar: Node pada Linked List
#=======================================================================================

class Node:
    # Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data
        self.next = None

#1) Membuat node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")


#2) Mendefinisikan head dan menghubungkan node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal: Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data)
    current = current.next