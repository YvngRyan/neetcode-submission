# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None
        dummy = None
        while second:
            tmp = second.next
            second.next = dummy
            dummy = second
            second = tmp
        
        curr = head
        while dummy:
            tmp1 = curr.next
            tmp2 = dummy.next

            curr.next = dummy
            dummy.next = tmp1
            curr = tmp1
            dummy = tmp2