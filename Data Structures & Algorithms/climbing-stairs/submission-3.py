class Solution:
    def climbStairs(self, n: int) -> int:
        x,y=1,1
        #...xy
        for i in range(n-1):
            temp=x
            x=x+y
            y=temp
        return x
