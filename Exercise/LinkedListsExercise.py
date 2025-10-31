class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Implement a singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != key:
            current = current.next
        if not current.next:
            return
        current.next = current.next.next
        
    def search(self,key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')

ll = SinglyLinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
ll.prepend(5)
ll.display()
ll.delete(0)

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data) 
        if self.head is None:
            head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def prepend(self, data):
       new_node = Node(data) 
       new_node.next = self.head
       self.head = new_node
       
    def delete(self, key):
        if not self.head:
            return
        if self.head.data == key:
            self.head = self.head.next 
            return
        current = self.head
        while current.next and current.next.data != key:
            current = current.next
        if current != key:
            return None
        current.next = current.next.next 

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
        
# Reverse a linked list (iterative & recursive).

# Detect a cycle in a linked list (Floyd’s cycle detection).

# Find the middle node of a linked list.

# Merge two sorted linked lists.

#LRU Cache