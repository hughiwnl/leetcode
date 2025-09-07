# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
        
# 1,2 2,4 3,6: while fast and fast.next means it will run until it hits null
# if fast and slow equal each other anad fast and fast.enxt arent null, its a loop