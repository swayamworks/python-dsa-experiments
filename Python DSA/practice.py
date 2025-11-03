class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class Stack:
    def __init__(self):
        self.top= None 
    def push(self, value):
        newnode= Node(value)
        newnode.next= self.top 
        self.top= newnode 
    def pop(self):
        if self.top is None:
            print("underflow")
        val= self.top.data
        self.top= self.top.next 
        return val
    def peek(self):
        if self.top is None:
            return None 
        return self.top.data
    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.data, end=" ")
            temp= temp.next 
        return
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Stack after push:")
s.display()

print("\nPopped:", s.pop())
print("After pop:")
s.display()

