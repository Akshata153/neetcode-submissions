class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        
        if len(self.stack):
            minm=float('inf')
            for i in range(len(self.stack)):
                minm=min(minm,self.stack[i])
            return minm
        return 
