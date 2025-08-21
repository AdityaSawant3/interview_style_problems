class Stack:

    def __init__(self, size):
        self.arr = [0] * size
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == len(self.arr)-1
    
    def push(self, element):
        if self.isFull():
            print("Stack overflow")
            return
        self.top += 1
        self.arr[self.top] = element

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return
        element = self.arr[self.top]
        self.top -= 1
        return element
    
    def peek(self):
        if self.isEmpty():
            print("Cannot retrive peek element")
            return
        return self.arr[self.top]
    
    def printStack(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        for i in range(self.top+1):
            print(self.arr[i])
    
s = Stack(5)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.printStack()

while not s.isEmpty():
    print(f"Peek element is {s.peek()}")
    print(f"{s.pop()} element popped")