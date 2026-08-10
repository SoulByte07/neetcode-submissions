class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        eleStack=[]
        indexStack=[]
        res=[0]*len(temperatures) # init with 0's
        for curr_i,e in enumerate(temperatures):
            if len(eleStack)==0: # isEmpty()
                eleStack.append(e)
                indexStack.append(curr_i)
                continue
            topEle=eleStack[-1]
            while topEle<e and len(eleStack)!=0:
                popedIndex=indexStack[-1]
                gap=curr_i-popedIndex
                res[popedIndex]=gap
                eleStack.pop(-1)
                indexStack.pop(-1)
                if len(eleStack)==0: # isEmpty()
                    break
                else:                # Not Empty
                    top=eleStack[-1]
            eleStack.append(e)
            indexStack.append(curr_i)
        return res
            
