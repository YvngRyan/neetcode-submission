class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            prevVal, prevMin = self.stack[-1]
            self.stack.append([val, min(prevMin, val)])
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        currVal, currMin = self.stack[-1]
        return currVal

    def getMin(self) -> int:
        currVal, currMin = self.stack[-1]
        return currMin
