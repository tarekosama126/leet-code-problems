class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return []
        else:
            self.stack.pop(len(self.stack) - 1)

    def top(self) -> int:
        if len(self.stack) == 0:
            return []
        else:
            return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return []
        else:
            return min(self.stack)