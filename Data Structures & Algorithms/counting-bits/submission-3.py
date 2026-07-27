class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]*(n+1)
        for n in range(n+1):
            res[n]=res[n>>1]+(n&1)
        return res

