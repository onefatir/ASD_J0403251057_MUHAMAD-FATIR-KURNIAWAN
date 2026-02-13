# ================================
# Praktikum 3: Linked List dan Implementasinya
# Latihan 1: Implementasikan fungsi	untuk menghapus	node dengan	nilai tertentu
# ================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail

    # Fungsi untuk menghapus node dengan nilai tertentu
    def delete_node(self, key):
        temp = self.head

        # Jika head node sendiri yang akan dihapus
        if temp and temp.data == key:
            self.head = temp.next
            # Update tail jika menghapus satu-satunya node
            if self.head is None:
                self.tail = None
            temp = None
            return

        # Cari node yang akan dihapus, simpan prev node
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
    
        # Jika key tidak ditemukan dalam linked list
        if temp is None:
            return
        
        # Unlink node dari linked list
        prev.next = temp.next
        # Update tail jika menghapus node terakhir
        if temp == self.tail:
            self.tail = prev
        temp = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head = new_node
            self.tail = new_node # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node # Sambungkan tail ke node baru
            self.tail = new_node # Update tail ke node baru
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# Contoh Penggunaan
ll = SingleLinkedList()
print("Sebelum menghapus:")
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.display()
# Menghapus node dengan nilai 5
ll.delete_node(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
print("Setelah menghapus:")
ll.display()