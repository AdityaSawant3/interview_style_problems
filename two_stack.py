class Stack:

    def __init__(self, size):
        self.arr = [0] * size
        self.top1 = -1
        self.top2 = len(self.arr)

    def isEmpty1(self):
        return self.top1 == -1
    
    def isEmpty2(self):
        return self.top2 == len(self.arr)
    
    def isFull(self):
        return self.top1 + 1 == self.top2
    
    def push1(self, element):
        if self.isFull():
            print("Stack overflow")
            return
        self.top1 += 1
        self.arr[self.top1] = element

    def push2(self, element):
        if self.isFull():
            print("Stack overflow")
            return
        self.top2 -= 1
        self.arr[self.top2] = element

    def pop1(self):
        if self.isEmpty1():
            print("Stack underflow")
            return
        element = self.arr[self.top1]
        self.arr[self.top1] = 0
        self.top1 -= 1
        return element
    
    def pop2(self):
        if self.isEmpty2():
            print("Stack underflow")
            return
        element = self.arr[self.top2]
        self.arr[self.top2] = 0
        self.top2 += 1
        return element

    def array(self):
        return self.arr

s = Stack(5)
s.push1(1)
s.push1(3)
s.push2(9)
s.push2(8)
s.push2(6)

s.pop1()

s.push2(12)

s.pop2()
s.pop2()
s.pop2()

s.push1(67)

ans = s.array()
print(ans)