class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            l=len(s)
            res+=str(l)+'#'+s
            # print(res.join(str(l)+'#'+s))
            # print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i,j=0,0
        while i <len(s):
            j=i
            while s[j]!='#':
                j+=1
            
            lt=s[i:j]
            l=int(lt)
            word=s[j+1:j+l+1]
            res.append(word)
            i=j+l+1
        return res
