class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        tempQ = self.q

        self.q = collections.deque()
        self.q.append(x)
        for n in tempQ:
            self.q.append(n)

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()