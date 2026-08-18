class TimeMap:

    def __init__(self):
        self.map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key]=[]
        self.map[key]=[[value,timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        res=""
        val=self.map.get(key,[])
        l,r=0,len(val)-1
        while l<=r:
            mid=(r+l)//2
            if val[mid][1]<=timestamp:
                res=val[mid][0]
                l=mid+1
            else:
                r=mid-1
        return res
