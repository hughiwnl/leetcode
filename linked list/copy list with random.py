"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old = { None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            old[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = old[cur]
            copy.next = old[cur.next]
            copy.random = old[cur.random]
            cur = cur.next
        return old[head]
    
'''
oldToCopy is like a lookup table — it doesn’t store the .next or .random itself.
The linked list exists in the copy nodes, which the dictionary points to.

random is its own variable/pointer

.random — it might point to a node we haven’t processed yet.
which is why we use a dictionary/hashmap
'''
