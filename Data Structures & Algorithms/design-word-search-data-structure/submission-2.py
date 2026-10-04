class Node:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=Node()
        

    def addWord(self, word: str) -> None:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=Node()     
            curr=curr.children[ch]
        curr.end=True   

    def search(self, word: str) -> bool:
        def dfs(j,curr):
            for i in range(j,len(word)):
                if word[i]=='.':
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    #move pointers in trie
                    if word[i] not in curr.children:
                        return False
                    curr=curr.children[word[i]]
            return curr.end
        return dfs(0,self.root)
        
        
