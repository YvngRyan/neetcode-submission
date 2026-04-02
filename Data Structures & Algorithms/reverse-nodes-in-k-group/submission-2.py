# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevKth = res = ListNode(0, head)
        
        while True:
            kth = self.getKth(prevKth, k)
            if not kth:
                break
            
            nxtKth = kth.next
            prev = nxtKth
            curr = prevKth.next # curr.next is pointing here

            while curr != nxtKth:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prevKth.next
            prevKth.next = kth
            prevKth = tmp
        return res.next
    

    def getKth(self, node, k):
        curr = node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
            