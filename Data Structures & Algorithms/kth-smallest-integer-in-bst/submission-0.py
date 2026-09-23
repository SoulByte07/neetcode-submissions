# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count=0
        self.res=None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root, k)
        return self.res

    def dfs(self, root, k):
        if not root or self.res is not None:
            return 
        self.dfs(root.left, k)
        self.count+=1
        if self.count==k:
            self.res=root.val
            return
        self.dfs(root.right,k)

        