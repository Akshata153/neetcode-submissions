class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        visited=set()

        def dfs(r,c,l):
            if l==len(word):
                return True
            
            if (r<0 or r>=rows or c<0 or c>=cols or board[r][c]!=word[l] or (r,c) in visited):
                return False
            
            visited.add((r,c))
            found=(dfs(r+1,c,l+1) or dfs(r-1,c,l+1) or dfs(r,c+1,l+1) or dfs(r,c-1,l+1))
            visited.remove((r,c))
            return found
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False