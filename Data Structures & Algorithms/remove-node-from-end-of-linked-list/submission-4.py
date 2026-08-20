# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=slow=head 
        curr=head
        tempN=1
        while tempN<=n: # fast will reach to n
            fast=fast.next
            tempN+=1
        if not fast:
            return head.next
        prev=None
        while fast and slow: # fast will reach end, slow will reach len(list)-n
            prev=slow
            slow=slow.next
            fast=fast.next
        prev.next=slow.next # delete nth element
        return curr


