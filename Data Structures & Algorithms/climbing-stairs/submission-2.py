class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[1]*(n+1)
        # print(arr)

        for i in range(n-2,-1,-1):
            # print("hi")
            arr[i]=arr[i+1]+arr[i+2]
        
        return arr[0]