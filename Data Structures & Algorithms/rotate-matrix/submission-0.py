class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        res = [[0 for _ in range(col)] for _ in range(row)]

        for r in range(row):
            for c in range(col):
                res[c][row-1-r] = matrix[r][c]

        for r in range(row):
            for c in range(col):
                matrix[r][c] = res[r][c]