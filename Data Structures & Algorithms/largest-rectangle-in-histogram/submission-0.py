class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack=[]
        area=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                height=heights[stack.pop()]
                if stack:
                   width=i-stack[-1]-1
                else:
                    width=i
                area=max(area,height *width)
            stack.append(i)

        return area

