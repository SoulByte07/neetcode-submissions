# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(root, isValid):
            if not root:
                return isValid
            if root.left:
                left=root.left.val
                isValid=isValid and left<root.val
            if root.right:
                right=root.right.val
                isValid=isValid and right>root.val
            return dfs(root.left, isValid)
            return dfs(root.right, isValid)
        return dfs(root, True)









