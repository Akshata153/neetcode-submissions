class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res=[]
        visited=set()
        rows=len(board)
        cols=len(board[0])
        def dfs(i,j,t):
            if t==len(word):
                return True
            if i<0 or i>=rows or j<0 or j>=cols or t>len(word) or board[i][j]!=word[t] or (i,j) in visited:
                return False
            
            visited.add((i,j))
            found=(dfs(i+1,j,t+1) or dfs(i,j+1,t+1) or dfs(i-1,j,t+1) or dfs(i,j-1,t+1))
            visited.remove((i,j))

            return found
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    
                    return True
        return False