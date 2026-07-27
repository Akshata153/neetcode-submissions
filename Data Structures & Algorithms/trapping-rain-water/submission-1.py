class Solution:
    def trap(self, height: List[int]) -> int:
        area=0
        l,r=0,len(height)-1
        bigl,bigr=height[0],height[r]
        while l<r:
            if height[r]>height[l]:
                if height[l]>bigl:
                    bigl=height[l]
                else:
                    area+=bigl-height[l]
                l+=1

            else:
                if height[r]>bigr:
                    bigr=height[r]
                else:
                    area+=bigr-height[r]
                r-=1
            print(area)
        return area