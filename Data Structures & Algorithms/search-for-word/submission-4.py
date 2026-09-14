class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        colns=len(board[0])

        def dfs(i,j,t):
            if t>=len(word):
                return True
            if i<0 or j<0 or i>=rows or j>=colns or board[i][j]!=word[t]:
                return False
            temp=board[i][j]
            board[i][j]="#"
            flag=(dfs(i+1,j,t+1) or dfs(i,j+1,t+1) or dfs(i-1,j,t+1) or dfs(i,j-1,t+1))
            board[i][j]=temp
            return flag

        for i in range(rows):
            for j in range(colns):
                if dfs(i,j,0):
                    return True
        return False
