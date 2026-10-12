class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i, subset, total):
            if total==target:
                if subset not in res:
                    res.append(subset.copy())
                return
            if total>target or i>=len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1, subset, total+candidates[i])
            subset.pop()
            dfs(i+1, subset, total)
        dfs(0, [], 0)
        return res