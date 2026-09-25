class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        grid=[['.']* n for i in range(n)]
        colset=set()
        posset=set()
        negset=set()
        def dfs(r):
            if r>=n:
                res.append(["".join(grid[r]) for r in range(n)])
                # print(res)
                return 
            for c in range(n):
                if (r+c) in posset or (r-c) in negset or c in colset:
                    continue
                grid[r][c]="Q"
                colset.add(c)
                posset.add(r+c)
                negset.add(r-c)

                dfs(r+1)

                grid[r][c]="."
                colset.remove(c)
                posset.remove(r+c)
                negset.remove(r-c)

        dfs(0)
        return res

                
