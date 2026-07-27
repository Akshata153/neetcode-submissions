class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0 for _ in range(len(temperatures))]
        stack=[]
        for i in range(len(temperatures)):
            # print(temperatures[i])
            # print(stack)
            
            while stack and temperatures[i]>temperatures[stack[-1]]:

                x=stack.pop()
                # print("pop: ",x)
                res[x]=i-x
                # print("res:",res)
            stack.append(i)

        return res