class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i, subset, total):
            if total==target:
                res.append(subset.copy())
                return
            if total>target or i>=len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1, subset, total+candidates[i])
            ele =subset.pop()
            try:
                while candidates[i+1]==ele:
                    i+=1
            except:
                i=i
            dfs(i+1, subset, total)
        dfs(0, [], 0)
        return res