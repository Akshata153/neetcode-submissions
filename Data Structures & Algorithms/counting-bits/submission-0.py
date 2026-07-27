class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for x in range(n+1):
            k=0
            for j in range(32):
                if x&1:
                    k+=1
                x=x>>1
            res.append(k)
        return res