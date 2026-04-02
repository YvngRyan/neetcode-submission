# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            res = dummy = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            
            if l1:
                dummy.next = l1
            if l2:
                dummy.next = l2
            
            return res.next

        while len(lists) > 1:
            currLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = None
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                
                mergedList = merge(list1, list2)
                currLists.append(mergedList)
            lists = currLists
        return lists[0] if lists else None
