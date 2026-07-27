class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxm=-1
        l=0
        r=len(heights)-1
        while l<r:
            area=(min(heights[l],heights[r]))*(r-l)
            maxm=area if area>maxm else maxm
            if heights[r]>heights[l]:
                
                l+=1
            else:
                r-=1
        return maxm