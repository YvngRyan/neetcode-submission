# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Unoptimal Solution Space Complexity O(N)
        # count = set()
        # curr = head
        # while curr:
        #     if curr in count:
        #         return True
        #     count.add(curr)
        #     curr = curr.next
        # return False

        #Optimal Solution Space Complexity O(1)
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False