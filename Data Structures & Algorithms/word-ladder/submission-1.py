import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordset=set()
        q=deque()

        for w in wordList:
            wordset.add(w)

        if endWord not in wordset:
            return 0

        map=defaultdict(list)

        for w in wordset:
            for i in range(len(w)):
                pattern=w[:i]+"*"+w[i+1:]
                map[pattern].append(w)

        # alp=string.ascii_lowercase
        q.append((beginWord,1))
        visited=set()
        visited.add(beginWord)
        while q:
            w,l=q.popleft()
            if w==endWord:
                return l
            for i in range(len(w)):
                pattern=w[:i]+"*"+w[i+1:]
                for newword in map[pattern]:
                    if newword not in visited:
                        visited.add(newword)
                        q.append((newword,l+1))
        return 0