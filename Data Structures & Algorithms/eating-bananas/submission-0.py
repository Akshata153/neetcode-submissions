class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minm=h
        l=1
        r=max(piles)
        minm=float('inf')
        while l<=r:
            k=(l+r)//2
            hr=0
            for i in range(len(piles)):
                hr+=math.ceil(piles[i]/k)
            if hr<=h:
                minm=k
                r=k-1
            else:
                l=k+1
            
            
        return minm