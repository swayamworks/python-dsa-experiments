class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def _init_(self):
        self.head = None

    def insert(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            new.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new
        new.next = self.head

    def delete(self, value):
        if self.head is None:
            return
        
        temp = self.head
        
        # deleting head
        if self.head.data == value:
            # find last node
            last = self.head
            while last.next != self.head:
                last = last.next
            # skip old head
            self.head = self.head.next
            last.next = self.head
            return
        
        # deleting non-head
        while temp.next != self.head and temp.next.data != value:
            temp = temp.next
        
        if temp.next.data == value:
            temp.next = temp.next.next

    def display(self):
        if self.head is None:
            return
        t = self.head
        while True:
            print(t.data, end=" ")
            t = t.next
            if t == self.head:
                break
        print()
