#=======================================================================================
# Nama    : Muhamad Fatir Kurniawan
# NIM     : J0403251057
# Kelas   : A1
#=======================================================================================

#=======================================================================================
# Implementasi Dasar: Stack
#=======================================================================================
class Node:
    # Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack ada operasi push(memasukkan head baru) dan pop (menghapus head)
# A -> B -> C -> None
class Stack:
    def __init__(self):
        self.top = None # Top menunjuk ke node paling atas (awalnya kosong)

    def push(self, data):
        # Membuat node baru dengan data yang diberikan
        new_node = Node(data)

        # Node baru menunjuk ke top saat ini
        new_node.next = self.top 
        
        # Top sekarang menjadi node baru
        self.top = new_node

        # B -> A -> None

    def tampilkan(self):
        current = self.top
        print("Top -> ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def is_empty(self):
        return self.top is None # Stack kosong jika top = None

    def peek(self): # Melihat data pada top tanpa menghapusnya
        if self.is_empty():
            print("Stack kosong, tidak bisa peek.")
            return None
        return self.top.data

    def pop(self): # Mengambil / menghapus node paling atas (top/head)
        if self.is_empty():
            print("Stack kosong, tidak bisa pop.")
            return None
        
        # Simpan data dari top yang akan di-pop
        popped_data = self.top.data
        
        # Top sekarang menjadi node berikutnya
        self.top = self.top.next
        
        return popped_data

# Instantiasi class stack
stack = Stack()
stack.push("A")
stack.pop() # Menghapus A
stack.push("B")
stack.push("C")
stack.tampilkan()
print("Top saat ini:", stack.peek()) # Melihat top tanpa menghapus