# ================================
# Praktikum 3: Linked List dan Implementasinya
# Latihan 1: Single Linked List
# ================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # Tambahkan pointer tail
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
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
ll.display()

# ================================
# Praktikum 3: Linked List dan Implementasinya
# Latihan 2: Doubly Linked List
# ================================

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
    
# Contoh Penggunaan
dll = DoublyLinkedList()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(13)
dll.insert_at_end(2)
dll.display_forward()
dll.display_backward()


# ================================
# Praktikum 3: Linked List dan Implementasinya
# Latihan 3: Circular Single Linked List
# ================================
class CircularSinglyLinkedList:
    def	__init__(self):
        self.head =	None
        self.tail =	None
    def	insert_at_end(self,	data):
        new_node = Node(data)
        if not self.head: # Jika linked list kosong
            self.head =	new_node 
            self.tail =	new_node
            self.tail.next = self.head # Circular link	kembali	ke	head
        else:
            self.tail.next = new_node # Sambungkan	tail ke	node baru
            self.tail = new_node # Update tail ke node baru
            self.tail.next = self.head # Circular link kembali ke head

    def	display(self):
        if not self.head:
            print("List	is	empty")
            return

        print("Circular	Linked List Traversal:")
        temp = self.head
        print(temp.data, end="->")
        temp = temp.next
        while temp != self.head:
            print(temp.data, end="->")
            temp = temp.next

        print("... (back to head)")

# Contoh Penggunaan
cll	= CircularSinglyLinkedList()
cll.insert_at_end(3)
cll.insert_at_end(5)
cll.insert_at_end(13)
cll.insert_at_end(2)
cll.display()