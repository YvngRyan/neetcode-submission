# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        res = dummy
        curr = head
        while n > 0:
            curr = curr.next
            n -= 1
        while curr:
            curr = curr.next
            dummy = dummy.next
        dummy.next = dummy.next.next

        return res.next