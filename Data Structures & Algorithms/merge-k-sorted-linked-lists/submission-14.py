# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(list1, list2):
            dummy = ListNode()
            curr = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            if list1:
                curr.next = list1
            if list2:
                curr.next = list2
            return dummy.next
        
        if not lists:
            return None

        while len(lists) > 1:
            currList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = None
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                mergedList = mergeLists(list1, list2)
                currList.append(mergedList)
            lists = currList
        return lists[0]