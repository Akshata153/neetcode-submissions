class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dep={c:set() for w in words for c in w}
        indegree={c:0 for c in dep}

        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            # print(f"{word1} {word2}")
            minlen=min(len(word1),len(word2))
            if len(word1)>len(word2) and word1[:minlen]==word2[:minlen]:
                return ""
            
            for j in range(minlen):
                if word1[j]!=word2[j]:
                    if word2[j] not in dep[word1[j]]:
                        dep[word1[j]].add(word2[j])
                        indegree[word2[j]]+=1
                    break
        q=deque([c for c in indegree if indegree[c]==0])
        res=[]
        while q:
            ch=q.popleft()
            res.append(ch)
            for neighb in dep[ch]:
                indegree[neighb]-=1
                if indegree[neighb]==0:
                    q.append(neighb)
        if len(res)!=len(dep):
            return ""
        return "".join(res)
