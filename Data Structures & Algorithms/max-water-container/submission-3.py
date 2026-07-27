class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maxm=float('-inf')
        curr=0
        while l<r:
            curr=(r-l)*min(heights[l],heights[r])
            maxm=max(maxm,curr)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxm
