class Stack:
    def __init__(self, cap):
        self.data = [None]* cap
        self.cap= cap
        self.top = -1
    def push(self, item):
        if self.top==self.cap-1:
            print("overflow")
            return None
        self.top +=1
        self.data[self.top]= item
    def pop(self):
        if self.top== -1:
            print("underflow")
            return None
        val = self.data[self.top]
        self.top -= 1
        return val
    def peek(self):
        return self.data[self.top] if self.top != -1 else None
    def size(self):
        return self.top + 1
    def display(self):
        return self.data[:self.top+1:]
