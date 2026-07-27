class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxm=0
        area=0
        count=0

        def dfs(i:int,j:int,count:int)->int:
            if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j]==0:
                return count
            
            count+=1
            grid[i][j]=0

            count=dfs(i+1,j,count)
            count=dfs(i,j+1,count)
            count=dfs(i-1,j,count)
            count=dfs(i,j-1,count)

            return count




        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count=0
                    area=dfs(i,j,count)
                    maxm=max(maxm,area)
        
        return maxm

