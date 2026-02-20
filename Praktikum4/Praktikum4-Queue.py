#=======================================================================================
# Nama    : Muhamad Fatir Kurniawan
# NIM     : J0403251057
# Kelas   : A1
#=======================================================================================

#=======================================================================================
# Implementasi Dasar: Queue
#=======================================================================================
class Node:
    # Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None # Node paling depan
        self.rear = None  # Node paling belakang

    def is_empty(self):
        return self.front is None # Queue kosong jika front = None

    # Membuat fungsi untuk menambahkan data baru
    def enqueue(self, data):
        nodeBaru = Node(data)
        if self.is_empty(): # Queue kosong
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        self.rear.next = nodeBaru # Rear saat ini menunjuk ke node baru
        self.rear = nodeBaru      # Rear sekarang menjadi node baru

    def dequeue(self):
        if self.is_empty(): # Queue kosong
            print("Queue kosong, tidak bisa dequeue.")
            return None
        
        dequeued_data = self.front.data # Simpan data yang akan di-dequeue
        self.front = self.front.next     # Front sekarang menjadi node berikutnya
        
        if self.is_empty(): # Jika setelah dequeue queue menjadi kosong, rear juga harus di-set ke None
            self.rear = None
        
        return dequeued_data

    def peek(self): # Melihat data pada front tanpa menghapusnya
        if self.is_empty():
            print("Queue kosong, tidak bisa peek.")
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None # Queue kosong jika front = None
    
    def tampilkan(self):
        current = self.front
        print("Front -> ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
print("Dequeue:", q.dequeue())
q.tampilkan()
print("Peek:", q.peek())
print("Dequeue:", q.dequeue())
q.tampilkan()