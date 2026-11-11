class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res=[[0]*n]*m
        
        # print(res)
        for i in range(0,m):
            for j in range(0,n):
                if i==0 or j==0:
                    res[i][j]=1
                    continue
                res[i][j]=res[i-1][j]+res[i][j-1]
        return res[-1][-1]
            
