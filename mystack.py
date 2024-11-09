class MyStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
class MyStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

class MyStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
