class PrefixTree:

    def __init__(self):
        self.myset=set()
        self.prefix=set()

    def insert(self, word: str) -> None:
        self.myset.add(word)
        for i in range(1,len(word)+1):
            self.prefix.add(word[:i])


    def search(self, word: str) -> bool:
        if word in self.myset:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.prefix

        
        