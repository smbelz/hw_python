class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append([x, x])
        else:
            self.stack.append([x, min(x, self.stack[-1][1])])

    def pop(self):
        elem = self.stack[-1][0]
        del self.stack[-1]
        return elem

    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]


stack = MyStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
print(stack.get_min())
stack.pop()
print(stack.top())
print(stack.get_min())
