class Solution:
    def reverse(self, x: int) -> int:
        org=x
        x=abs(x)
        res=int(str(x)[::-1])
        if org<0:
            res=res*-1
        if res<-(1<<31) or res> (1<<31):
            return 0
        else:
            return res