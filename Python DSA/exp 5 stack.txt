class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        newnode = Node(value)
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        return

# ----------- Example -----------
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack after push:")
s.display()

print("\nPopped:", s.pop())
print("After pop:")
s.display()
