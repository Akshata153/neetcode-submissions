class Node:
    def __init__(self):
        self.children={}
        self.end=False

class Solution:
    def add(self,word,curr):
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=Node()
            curr=curr.children[ch]
        curr.end=True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Node()
        curr=root
        for word in words:
            self.add(word,curr)
        
        rows=len(board)
        cols=len(board[0])
        res=[]
        visited=set()

        def dfs(i,j,word,curr):
            if i<0 or i>=rows or j<0 or j>=cols or board[i][j] not in curr.children or (i,j) in visited:
                return 
            visited.add((i,j))
            curr=curr.children[board[i][j]]
            word+=board[i][j]
            if curr.end:
                res.append(word)
                curr.end=False

            dfs(i+1,j,word,curr)
            dfs(i-1,j,word,curr)
            dfs(i,j+1,word,curr)
            dfs(i,j-1,word,curr)

            visited.remove((i,j))
            return


        for i in range(rows):
            for j in range(cols):
                dfs(i,j,"",root)

        return res