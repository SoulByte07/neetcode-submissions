# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        anshead=ListNode(0)
        dummy=anshead
        carry=0
        carryChange=0
        while l1 or l2 or carryChange:
            # default=0 for large nums
            if not carryChange:
                carry=0
            if l1:
                v1=l1.val
            else:
                v1=0
            if l2:
                v2=l2.val
            else:
                v2=0
            # sum
            s=v1+v2+carry
            # large nums
            if s>9:
                onceDigit=s%10
                tensDigit=s//10
                carry=tensDigit
                carryChange=1
                s=onceDigit
            else:
                carryChange=0
            # attach the ans
            newNode=ListNode(s)
            dummy.next=newNode
            dummy=dummy.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next

        return anshead.next
        
            


            