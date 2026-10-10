class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        fresh=set()
        q=deque()
        rows,cols=len(grid),len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append([i,j])
                    visited.add((i,j))
                elif grid[i][j]==1:
                    fresh.add((i,j))
        t=-1
        def addNB(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0 or (r,c) in visited:
                return
            
            fresh.remove((r,c))
            q.append([r,c])
            visited.add((r,c))
            
        if not q:
            return 0 if not len(fresh) else -1
        while q:
            # print(q)
            for i in range(len(q)):
                r,c=q.popleft()
                addNB(r+1,c)
                addNB(r,c+1)
                addNB(r-1,c)
                addNB(r,c-1)
            t+=1
            # print(t)
        return t if not len(fresh) else -1


