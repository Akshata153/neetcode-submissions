class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        visited=set()

        min_heap=[(grid[0][0],0,0)]
        visited.add((0,0))

        directions=[(0,1),(1,0),(0,-1),(-1,0)]

        while min_heap:
            t,r,c=heapq.heappop(min_heap)
            print(f"pop: {t} {r} {c}")

            if r==n-1 and c==n-1:
                return t
            
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                print(f"Direction: {nr} {nc}")

                if 0<=nr<n and 0<=nc<n and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    new_t=max(t,grid[nr][nc])
                    print(f"push {new_t} {nr} {nc}")

                    heapq.heappush(min_heap,(new_t,nr,nc))
        return -1