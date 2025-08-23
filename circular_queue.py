# Circular queue

class CircularQueue:

    def __init__(self, capacity):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.size = 0
        self.front = -1
        self.rear = -1

    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.front == -1
    
    def enqueue(self, element):
        if self.isFull():
            print("Queue is full, cannot insert element.")
            return
        if self.isEmpty():
            self.front = 0
            self.rear = 0

            # When adding element first time insert value at first index.
            self.arr[self.rear] = element
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.arr[self.rear] = element
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, cannot remove element.")
            return
        
        removed_element = self.arr[self.front]
        self.arr[self.front] = 0
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return removed_element
    
    def printQueue(self):
        if self.isEmpty():
            print("queue is empty, cannot retrive elements")
            return
        print("Queue elements: ", end=" ")
        i = self.front
        count = 0

        while count < self.size:
            print(self.arr[i], end=" ")
            i = (i + 1) % self.capacity
            count += 1

        print("\n------------------------------------------")

q = CircularQueue(4)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.printQueue()

q.dequeue()
q.dequeue()

q.printQueue()

q.enqueue(7)
q.enqueue(8)

q.printQueue()