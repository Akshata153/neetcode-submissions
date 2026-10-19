class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set()
        for w in wordList:
            wordset.add(w)
        if endWord not in wordList:
            return 0
        
        map=defaultdict(list)
        for w in wordset:
            for i in range(len(w)):
                pattern=w[:i]+"*"+w[i+1:]
                map[pattern].append(w)

        q=deque()
        q.append((beginWord,1))
        while q:
            w,l=q.popleft()
            if w==endWord:
                return l
            
            for i in range(len(w)):
                pattern=w[:i]+"*"+w[i+1:]
                for newword in map[pattern]:
                    if newword in wordset:
                        wordset.remove(newword)
                        q.append((newword,l+1))
        return 0
