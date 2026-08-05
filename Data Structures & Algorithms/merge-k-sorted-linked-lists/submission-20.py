# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            newList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                if list2:
                    mergedList = self.merge(list1, list2)
                    newList.append(mergedList)
                else:
                    newList.append(list1)
            lists = newList
        
        return lists[0]


    def merge(self, list1, list2):
        dummy = res = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        if list1:
            dummy.next = list1

        if list2:
            dummy.next = list2
        
        return res.next