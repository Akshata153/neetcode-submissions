class PrefixTree:

    def __init__(self):
        self.pref=set()
        self.wordset=set()

    def insert(self, word: str) -> None:
        self.wordset.add(word)
        for i in range(len(word)+1):
            self.pref.add(word[:i])


    def search(self, word: str) -> bool:
        if word in self.wordset:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        # print(self.pref)
        return prefix in self.pref

        
        