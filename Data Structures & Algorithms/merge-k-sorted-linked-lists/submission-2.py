# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        heap=[]

        # init the heads
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val,i,lists[i]))
        
        # actual code
        while heap:
            minVal, listIndex, node=heapq.heappop(heap)
            curr.next=node
            curr=curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, listIndex, node.next))
        return dummy.next
