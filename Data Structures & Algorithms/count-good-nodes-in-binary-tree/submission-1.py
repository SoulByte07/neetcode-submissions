# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxSeen=float('-inf')
        res=0
        def dfs(root, maxSeen):
            if not root:
                return None
            nonlocal res
            if root.val>=maxSeen:
                res+=1
            maxSeen=max(root.val, maxSeen)
            dfs(root.left, maxSeen)
            dfs(root.right, maxSeen)
        dfs(root, maxSeen)
        return res
            
