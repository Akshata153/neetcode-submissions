class Node:
    def __init__(self):
        self.children={}
        self.end=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def add(word,curr):
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch]=Node()
                curr=curr.children[ch]
            curr.end=True

        root=Node()
        for word in words:
            add(word,root)
        rows=len(board)
        cols=len(board[0])
        res=[]
        visited=set()

        def dfs(i,j,word,curr):
            if i<0 or i>=rows or j<0 or j>=cols or board[i][j] not in curr.children or (i,j) in visited:
                return
            word+=board[i][j]
            curr=curr.children[board[i][j]]
         
            if curr.end:
                print("**",word)
                res.append(word)
                curr.end=False
            visited.add((i,j))
            dfs(i+1,j,word,curr)
            dfs(i,j+1,word,curr)
            dfs(i-1,j,word,curr)
            dfs(i,j-1,word,curr)
            visited.remove((i,j))
            return



        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                   
                    dfs(i,j,"",root)
        return res