# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find half way point first, then reverse the second half
        #Then merge the reverse second half with the first half, 1 by 1

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #splitting the list in half
        prev = slow
        slow = slow.next
        prev.next = None

        #reversing the second list
        dummy = None
        while slow:
            temp = slow.next
            slow.next = dummy
            dummy = slow
            slow = temp
        
        #merge the two lists together
        first, second = head, dummy
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2