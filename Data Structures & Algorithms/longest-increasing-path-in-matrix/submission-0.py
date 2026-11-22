class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}

        def dfs(i,j,prev):
            if i<0 or j<0 or i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]<=prev:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res=1
            res=max(res,dfs(i+1,j,matrix[i][j])+1)
            res=max(res,dfs(i,j+1,matrix[i][j])+1)
            res=max(res,dfs(i,j+1,matrix[i][j])+1)
            res=max(res,dfs(i-1,j,matrix[i][j])+1)
            res=max(res,dfs(i,j-1,matrix[i][j])+1)
            dp[(i,j)]=res
            return res
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i,j,-1)
        return max(dp.values())