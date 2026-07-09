# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        second=head
        first=None
        while second:
            first=second.next
            second=second.next.next
        mid=first
        # Reverse
        prev=None
        while first:
            prev=first
            temp=first.next
            first.next=prev
            first=temp
        



