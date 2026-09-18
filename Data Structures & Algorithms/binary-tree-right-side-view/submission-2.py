# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=collections.deque()
        res=[]
        q.append(root)
        while q:
            rightEle=q[-1]
            res.append(rightEle.val)
            for i in range(len(q)):
                leftEle=q.popleft()
                if leftEle.left:
                    q.append(leftEle.left)
                if leftEle.right:
                    q.append(leftEle.right)
        return res
