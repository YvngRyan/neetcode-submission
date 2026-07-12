class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next

        while index > 0 and curr.next:
            curr = curr.next
            index -= 1
        
        return curr.val if curr != self.tail and index == 0 else -1
            

    def addAtHead(self, val: int) -> None:
        tmp = self.head.next
        self.head.next = ListNode(val, tmp, self.head)
        tmp.prev = self.head.next


    def addAtTail(self, val: int) -> None:
        tmp = self.tail.prev
        self.tail.prev = ListNode(val, self.tail, tmp)
        tmp.next = self.tail.prev

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head

        while index > 0 and curr.next:
            index -= 1
            curr = curr.next
        
        if not (index > 0 or curr == self.tail):
            tmp = curr.next
            curr.next = ListNode(val, tmp, curr)
            tmp.prev = curr.next


    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next

        while index > 0 and curr.next:
            index -= 1
            curr = curr.next
        
        if curr != self.tail:
            prev = curr.prev
            next = curr.next
            prev.next = next
            next.prev = prev
            curr.next = None
            curr.prev = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)