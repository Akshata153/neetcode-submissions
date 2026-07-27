class Solution:
    def trap(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        water=0
        L,R=l,r
        while l<r:
            # print(f"{l}:{r}")
            # print(f"{heights[L]}:::{heights[R]}")
            if heights[l]<heights[r]:
                if heights[L]<heights[l]:
                    L=l
                else:
                    # print(f"{(l-L)}*{heights[l]}")
                    water+=(heights[L]-heights[l])
                l+=1

            else:
                if heights[r]>heights[R]:
                    R=r
                else:
                    # print(f"{(R-r)}*{heights[r]}")
                    water+=(heights[R]-heights[r])
                r-=1
            # print("water: ",water)
        return water


