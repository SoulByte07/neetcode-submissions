class Solution:
    def isValidSudoku(self, arr: List[List[str]]) -> bool:
        col=collections.defaultdict(set)
        row=collections.defaultdict(set)
        diagnol=collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if arr[r][c]=='.':
                    continue
                if (arr[r][c]  in col[c] or
                arr[r][c]  in row[r] or
                arr[r][c]  in diagnol[(r//3),(c//3)]):
                    return False
                col[c].add(arr[r][c])
                row[r].add(arr[r][c])
                diagnol[(r//3,c//3)].add(arr[r][c])
        return True