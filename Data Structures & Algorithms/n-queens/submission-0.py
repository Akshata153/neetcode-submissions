class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        neg=set()
        pos=set()

        res=[]
        b=[["."]*n for i in range(n)]

        def dfs(r):
            if r==n:
                res.append(["".join(r) for r in b])
                return
            for c in range(n):
                if c in col or (r+c) in pos or (r-c) in neg:
                    continue
                b[r][c]="Q"
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)

                dfs(r+1)

                b[r][c]="."
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        dfs(0)
        return res
