class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])-1
        top, bottom = 0, len(matrix)-1

        while left<right and top<bottom:
            for i in range(left,right):
                res.append(matrix[top][i])
            for i in range(top, bottom):
                res.append(matrix[i][right])
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
            left+=1
            right-=1
            top+=1
            bottom-=1
        while left<=right and bottom==top:
            res.append(matrix[top][left])
            left+=1
        while left==right and bottom>=top:
            res.append(matrix[top][left])
            top+=1
        return res
