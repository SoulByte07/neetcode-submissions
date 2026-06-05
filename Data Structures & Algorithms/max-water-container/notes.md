```
if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
```
```
if flag:
                left+=1
                flag=1
            else:
                right-=1
                flag=0
```
flag wasnt works because of even odd, we have to move efficiently
