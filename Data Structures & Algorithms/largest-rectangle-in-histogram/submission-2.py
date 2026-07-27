class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxm=float('-inf')
        for i in range(len(heights)):
            j=i
            # maxm=max(maxm,heights[i])
            while stack and heights[i]<=stack[-1][0]:
                v,j=stack.pop()
                # print(f"{v}:{j}")
                maxm=max(maxm,(v*(i-j)))
                # print("maxm=",maxm)
            stack.append([heights[i],j])
            # print(stack)

        while stack:
            v,j=stack.pop()
            maxm=max(maxm,(len(heights)-j)*v)
            # print((len(heights)-j)*v)


        return maxm