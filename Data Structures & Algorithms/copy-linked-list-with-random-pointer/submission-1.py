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
        if head is None:
            return None
        og=head
        while og:
            clone=Node(og.val)
            clone.next=og.next
            og.next=clone
            og=clone.next
        
        newHead=head.next
        og=head
        while og:
            if og.random is not None:
                og.next.random=og.random.next
            og=og.next.next
        
        og=head
        while og:
            clone=og.next
            og.next=clone.next
            if clone.next is not None:
                clone.next=clone.next.next
            og=og.next
        return newHead



















