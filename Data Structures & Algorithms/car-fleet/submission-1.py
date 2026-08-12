class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        for i in range(len(position)):
            t=(target-position[i])/speed[i]
            time.append(t)

        position,time=zip(*sorted(zip(position,time),reverse=True))
        maxSoFar=0
        res=0
        for i in range(len(position)):
            if time[i]>maxSoFar:
                res+=1
                maxSoFar=time[i]
        return res       

            