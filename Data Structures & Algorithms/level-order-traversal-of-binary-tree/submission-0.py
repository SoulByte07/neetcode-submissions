# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            level=[]
            qLen=len(q)
            for i in range(qLen):
                qLeft=q.popleft()
                if qLeft:
                    level.append(qLeft.val)
                    q.append(qLeft.left)
                    q.append(qLeft.right)
            if level:
                res.append(level)
        return res