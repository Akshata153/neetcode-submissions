class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pac=set()
        atl=set()
        res=[]
        
        def dfs(r,c,visited,prev):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visited or heights[r][c]<prev:
                return
            
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            return


        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        
        for i in range(rows):
            for j in range(cols):
                if (i,j) in atl and (i,j) in pac:
                    res.append([i,j])
        
        return res