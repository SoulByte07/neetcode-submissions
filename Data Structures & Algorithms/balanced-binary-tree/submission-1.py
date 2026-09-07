# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        self.leftLen=self.rightLen=0
        def dfs(node):
            if not node:
                return 0
            self.leftLen=1+dfs(node.left)
            self.rightLen=1+dfs(node.right)
            diff=abs(self.leftLen-self.rightLen)
            if diff>1:
                return False
            else:
                return diff
        dfs(root)
        return True
