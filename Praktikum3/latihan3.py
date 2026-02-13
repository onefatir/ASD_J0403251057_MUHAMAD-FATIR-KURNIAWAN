# ================================
# Praktikum 3: Linked List dan Implementasinya
# Latihan 3: Implementasikan Pencarian pada node tertentu Double Linked List.
# ================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Untuk Doubly Linked List


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Menyimpan node terakhir untuk traversing mundur

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
 
    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")
    
    def search(self, key):
        if not self.head:
            print("Doubly linked list kosong. Tidak dapat mencari elemen.")
            return

        temp = self.head
        position = 0
        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam doubly linked list.")
                return
            temp = temp.next
            position += 1
        print(f"Elemen {key} tidak ditemukan dalam doubly linked list.")
    
# Contoh Penggunaan
dll = DoublyLinkedList()

angkaUser = input("Masukkan elemen ke dalam Doubly Linked List: ").split(", ")
for num in angkaUser:
    dll.insert_at_end(int(num.strip()))

key = input("Masukkan elemen yang ingin dicari: ").strip()
dll.search(int(key))
