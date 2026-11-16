class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dep={c:set() for word in words for c in word}
        indeg={c:0 for c in dep}

        #build 
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            # print(f"{w1} {w2}")

            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""

            for j in range(minlen):
                # print(f"{w1[j]}  {w2[j]}")
                if w1[j]!=w2[j]:
                    if w2[j] not in dep[w1[j]]:
                        dep[w1[j]].add(w2[j])
                        indeg[w2[j]]+=1
                    break
    
                
        q=deque([c for c in indeg if indeg[c]==0])
        res=[]

        while q:
            x=q.popleft()

            res.append(x)
            for n in dep[x]:
                indeg[n]-=1

                if indeg[n]==0:
                    q.append(n)

        return "".join(res) if len(res)==len(indeg) else ""
                

