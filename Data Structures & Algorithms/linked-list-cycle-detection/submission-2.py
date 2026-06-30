# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        map={}
        curr=head
        while curr:
            if curr.val in map:
                return True
            map[curr]=True
            curr=curr.next
        return False
