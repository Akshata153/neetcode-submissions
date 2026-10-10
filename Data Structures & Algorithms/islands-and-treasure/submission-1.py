class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        q=deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    q.append([i,j])
                    visited.add((i,j))
        
        dist=0

        def addneighbors(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==-1 or (r,c) in visited:
                return
            visited.add((r,c))
            q.append([r,c])
            return

        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist
                addneighbors(r+1,c)
                addneighbors(r,c+1)
                addneighbors(r-1,c)
                addneighbors(r,c-1)
            dist+=1
        

        