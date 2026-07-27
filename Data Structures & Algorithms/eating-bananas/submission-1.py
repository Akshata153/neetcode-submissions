class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            hr=0
            for i in range(len(piles)):
                hr+=math.ceil(piles[i]/k)
                # hr+=piles[i]//k
            # print(f"{k} rate: {hr}hrs")
            
            if hr<=h:
                # res=k
                r=k-1
            else:
                l=k+1
            # print(res)
        return l
        
