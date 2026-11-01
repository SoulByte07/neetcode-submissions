class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        maxReach = 0
        res = 0
        for i in range(len(gas)):
            maxReach = (gas[i]-cost[i])
            if maxReach<0:
                res = (i+1)%len(gas)
                maxReach = 0

        return res
                
