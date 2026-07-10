# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length
        curr=head
        len=0
        while curr:
            len+=1
            curr=curr.next
        # pivot
        prev_len=len-n
        curr=head
        for _ in range(prev_len):
            curr=curr.next
        curr.next=curr.next.next
            
        return head