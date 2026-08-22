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
        while l1 and l2:
            # default=0 for large nums
            if not carryChange:
                carry=0
            v1=l1.val
            v2=l2.val
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
            l1=l1.next
            l2=l2.next
        # attach remaining list
        if carryChange:
            newNode=ListNode(carry)
            dummy.next=newNode
            dummy=dummy.next
        if l1:
            dummy.next=l1
        if l2:
            dummy.next=l2
        return anshead.next
        
            


            