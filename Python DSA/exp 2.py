class Stack:
    def __init__(self, cap):
        self.data = [None] * cap
        self.cap = cap
        self.top = -1

    def push(self, item):
        if self.top == self.cap - 1:
            return
        self.top += 1
        self.data[self.top] = item

    def pop(self):
        if self.top == -1:
            return None
        val = self.data[self.top]
        self.top -= 1
        return val

    def peek(self):
        if self.top == -1:
            return None
        return self.data[self.top]

    def size(self):
        return self.top + 1

    def display(self):
        for i in range(self.top, -1, -1):
            print(self.data[i], end=" ")
        print()


def sort_stack(s):
    t = Stack(s.cap)
    while s.size() > 0:
        x = s.pop()
        while t.size() > 0 and t.peek() > x:
            s.push(t.pop())
        t.push(x)
    return t


s = Stack(10)
s.push(3)
s.push(1)
s.push(4)
s.push(2)

s.display()
sort_stack(s)
s.display()
