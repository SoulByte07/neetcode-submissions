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
            if root.left and root.right:
                isValid=isValid and root.left.val<root.val
                isValid=isValid and root.right.val>root.val
            return (dfs(root.left, isValid) and
            dfs(root.right, isValid))
        return dfs(root, (root.left.val<root.val if root.left else True) or (root.right.val>root.val if root.right else True))









