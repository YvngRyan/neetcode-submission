# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        cnt = head
        while cnt:
            cnt = cnt.next
            length += 1
        
        target = length - n
        if target == 0:
            return head.next

        tmp = head
        for i in range(target):
            if i == target - 1:
                tmp.next = tmp.next.next
            tmp = tmp.next
        return head