import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        # operators= {"+", "-", "*", "/"} 
        res=0
        opMap = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        for i,e in enumerate(tokens):
            if e in opMap:
                topOp1=stack[-1]
                stack.pop(-1)
                topOp2=stack[-1]
                stack.pop(-1)
                res+=int(opMap[e](topOp2,topOp1))
                stack.append(res)
            else:
                stack.append(e)
        return res

