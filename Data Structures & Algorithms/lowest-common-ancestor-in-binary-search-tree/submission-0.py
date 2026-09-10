# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pv,qv=min(p.val,q.val),max(p.val,q.val)
        if root.val>=pv and root.val<=qv:
            return root.val
        elif root.val<=pv and root.val<=qv:
            return self.lowestCommonAncestor(root.right, p, q)
        else :
            return self.lowestCommonAncestor(root.left, p,q)