class ListNode:
    def __init__(self, url=None, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, None, self.curr)

        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev != None:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next != None:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)