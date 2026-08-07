class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[float('infinity')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        minEle=min(val,self.minStack[-1])
        self.minStack.append(minEle)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]

        
