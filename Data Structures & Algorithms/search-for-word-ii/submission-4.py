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
        for word in words:
            self.add(word,root)

        

        res=[]
        visited=set()
        rows=len(board)
        cols=len(board[0])

        def dfs(i,j,curr,word):
            if i<0 or i>=rows or j<0 or j>=cols or board[i][j] not in curr.children or (i,j) in visited:
                return False
            visited.add((i,j))
            curr=curr.children[board[i][j]]
            word+=board[i][j]
            if curr.end:
                res.append(word)
                curr.end=False
            dfs(i+1,j,curr,word)
            dfs(i,j+1,curr,word)
            dfs(i-1,j,curr,word)
            dfs(i,j-1,curr,word)
            visited.remove((i,j))


        for i in range(rows):
            for j in range(cols):
                # print(res)
                dfs(i,j,root,"")


        return res