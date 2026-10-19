import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set()
        for w in wordList:
            wordset.add(w)
        
        if endWord not in wordset:
            return 0

        q=deque()
        q.append((beginWord,1))
        alp=string.ascii_lowercase
        while q:
            w,l=q.popleft()
            if w==endWord:
                return l
            for i in range(len(w)):
                for ch in alp:
                    newword=w[:i]+ch+w[i+1:]
                    if newword in wordset:
                        wordset.remove(newword)
                        q.append((newword,l+1))
        return 0
