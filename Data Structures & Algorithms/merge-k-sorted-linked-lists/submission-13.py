# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            currLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = None
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                mergedList = self.mergeLists(list1, list2)
                currLists.append(mergedList)
            lists = currLists
        return lists[0]
    def mergeLists(self, list1, list2):
        curr = ListNode()
        res = curr
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return res.next