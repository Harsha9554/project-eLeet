class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.is_empty():
            if self.min_stack[-1] == self.stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
