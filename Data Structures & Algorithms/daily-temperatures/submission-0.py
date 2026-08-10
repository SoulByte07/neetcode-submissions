class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        eleStack=[]
        indexStack=[]
        res=[]
        for curr_i,e in enumerate(temperatures):
            if len(eleStack)==0: # isEmpty()
                eleStack.append(e)
                indexStack.append(curr_i)
                continue
            top=eleStack[-1]
            while top<e:
                gap=curr_i-indexStack[-1]
                res.append(gap)
                eleStack.pop(-1)
                indexStack.pop(-1)
                if len(eleStack)==0: # isEmpty()
                    break
                else:                # Not Empty
                    top=eleStack[-1]
            eleStack.append(e)
            indexStack.append(curr_i)
        for _ in eleStack:
            res.append(0)
        return res
            
