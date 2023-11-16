class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self) -> str:
        return str(self.stack)

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
