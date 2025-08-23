class Queue:

    def __init__(self, size):
        self.arr = [0] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear
    
    def isFull(self):
        return self.rear == self.size-1
    
    def enqueue(self, element):
        if self.isFull():
            print("Cannot enqueue element. Queue is full")
            return
        if self.isEmpty():
            self.front = 0
        self.rear += 1
        self.arr[self.rear] = element

    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue element. Queue is empty")
            return
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
            print("Dequeued")
            print("\n---------------------------")
        
    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        for i in range(self.front, self.rear+1):
            print(self.arr[i], end=" ")

        print("\n---------------------------")
    
    def getFront(self):
        if self.isEmpty():
            print("Cannot return front element. Queue is empty")
            return
        return self.arr[self.front]

    def getRear(self):
        if self.isEmpty():
            print("Cannot return rear element. Queue is empty")
            return
        return self.arr[self.rear]

queue = Queue(5)

queue.enqueue(73)
queue.enqueue(23)
queue.enqueue(56)
queue.enqueue(67)
queue.enqueue(19)
# queue.enqueue(39)

queue.printQueue()

while not queue.isEmpty():
    print(f"Front element of queue: {queue.getFront()}")
    print(f"Rear element of queue: {queue.getRear()}")
    queue.dequeue()
queue.printQueue()