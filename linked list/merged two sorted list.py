# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode() #starting point of merged list to avoid edge cases
        merged = head #also same as head
        while list1 and list2:
            if list1.val < list2.val:
                merged.next = list1
                list1 = list1.next 
            else:
                merged.next = list2
                list2 = list2.next
            merged = merged.next # tail pointer to update merged list, this is only while the list exists because either l1 or l2 will be added compared to when only 1 is left 
        if list1: # if one of the lists still exist then it will add it to the list
            merged.next = list1
        elif list2:
            merged.next = list2
        return head.next
    #merged.next and head.next and l1.next etc is the WHOLE list. merged = merge.next moves the pointer to the next one and they decide which one is next, and if one of them is empty, it sends in the whole list, same as head.next