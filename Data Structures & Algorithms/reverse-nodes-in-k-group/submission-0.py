
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 1. Create the dummy node and point it to our head
        dummy = ListNode(0, head)
        # groupPrev acts as our 'anchor' (prevGroupTail)
        groupPrev = dummy
        
        while True:
            # 2. Check if we have k nodes left to reverse
            kth = self.getKth(groupPrev, k)
            if not kth:
                break # Not enough nodes left, leave as is
                
            groupNext = kth.next
            
            # 3. Reverse the group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 4. Connect the reversed group back to our anchor
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next
        
    def getKth(self, curr: ListNode, k: int) -> ListNode:
        """Helper to find the kth node from the current position."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# --- Sample Input ---
# head = [1 -> 2 -> 3 -> 4 -> 5], k = 3

# --- Expected Output ---
# [3 -> 2 -> 1 -> 4 -> 5]