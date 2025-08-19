# Fixed size stack.

class Stack:

    def __init__(self, length):
        self.arr = [0] * length
        self.top = -1

    def isFull(self):
        return self.top == len(self.arr)-1
    
    def isEmpty(self):
            return self.top == -1
    
    def push(self, element):
        if self.isFull():
            print("Full!, cannot push element")
            return
        self.top += 1
        self.arr[self.top] = element

    def pop(self):
        if self.isEmpty():
            print("Empty! Cannot remove element")
            return
        element = self.arr[self.top]
        self.arr[self.top] = 0
        self.top -= 1
        print(f"Element poped: {element}")
    
    
    def printStack(self):
        for i in range(self.top+1):
            print(self.arr[i])

    def peek(self):
        if self.isEmpty():
            print("Cannot return element, because it is empty")
            return
        return self.arr[self.top]

s = Stack(5)
s.push(4)
s.push(3)
s.push(1)
s.push(2)
s.push(67)
s.push(3)
s.pop()
s.pop()
s.printStack()

print(f"Peek element is {s.peek()}")