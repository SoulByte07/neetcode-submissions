class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowL,rowR=0,len(matrix)-1
        colL,colR=0,len(matrix[0])-1
        while rowL<=rowR or colL<=colR:
            rowMid=rowL+((rowR-rowL)//2)
            colMid=colL+((colR-colL)//2)
            if matrix[rowMid][colMid]==target:
                return True
            elif matrix[rowMid][colMid]<target:
                rowR=rowMid-1
                colR=colMid-1
            else:
                rowL=rowMid+1
                colL=colMid+1
        return False