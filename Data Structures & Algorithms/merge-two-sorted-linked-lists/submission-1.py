# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        elif list1 and not list2:
            return list1
        elif not list1 and not list2:
            return None
        curr1 = list1
        curr2 = list2
        res = None
        #Initialize the result value to the node that is less than, but set
        #To list1 node if they are equal
        if curr1.val <= curr2.val:
            res = curr1
            curr1 = curr1.next
        else:
            res = curr2
            curr2 = curr2.next

        temp = res
        while curr1 or curr2:
            #If one of the linked lists has ended, then set the remaining to the
            #linked list that still has nodes
            if curr1 and not curr2:
                temp.next = curr1
                return res
            elif not curr1 and curr2:
                temp.next = curr2
                return res
            
            if curr1.val < curr2.val:
                temp.next = curr1
                temp = temp.next
                curr1 = curr1.next
            else:
                temp.next = curr2
                temp = temp.next
                curr2 = curr2.next
        return res
