class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        maxl=height[0]
        r=len(height)-1
        maxr=height[r]
        water=0
        while l<r:
            if height[l]<height[r]:
                if maxl<height[l]:
                    maxl=height[l]
                else:
                    water+=maxl-height[l]
                l+=1
            else:
                if maxr<height[r]:
                    maxr=height[r]
                else:
                    water+=maxr-height[r]
                r-=1
        return water