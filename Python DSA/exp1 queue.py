class Queue:
    def __init__(self, cap):
        self.data= [None] * cap
        self.cap= cap
        self.rear = -1
        self.front = 0
    def enqueue(self,value):
        if self.rear == self.cap -1:
            print("overflow")
            return None
        self.rear +=1
        self.data[self.rear]= value
    def dequeue(self):
        if self.front > self.rear:
            print("underflow")
            return None
        val = self.data[self.front]
        self.front +=1
        return val
    def display(self):
        return self.data[self.front : self.rear + 1:]
q= Queue(3)
q.enqueue(6)
q.enqueue(7)
q.enqueue(4)
print(q.display())
q.dequeue()
print(q.display())