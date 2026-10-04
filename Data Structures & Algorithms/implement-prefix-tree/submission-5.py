class Node:
    def __init__(self):
        self.children={}
        self.isend=False

class PrefixTree:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None: 
        curr=self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch]=Node() #create a node
            curr=curr.children[ch] #move to the next node
        curr.isend=True


    def search(self, word: str) -> bool:
        curr=self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return curr.isend
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr=curr.children[ch]
        return True

        
        