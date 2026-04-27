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
        paste = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            paste[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = paste[cur]
            copy.next = paste[cur.next]
            copy.random = paste[cur.random]
            cur = cur.next
        
        return paste[head]