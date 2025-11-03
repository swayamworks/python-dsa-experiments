class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        newnode = Node(value)
        if self.front is None:
            self.front = self.rear = newnode
            return
        self.rear.next = newnode
        self.rear = newnode

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return val

    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        return

# ----------- Example -----------
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)

print("Queue after enqueue:")
q.display()

print("\nDequeued:", q.dequeue())
print("After dequeue:")
q.display()
