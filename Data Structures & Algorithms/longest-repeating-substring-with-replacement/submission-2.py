class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxm_freq=0
        l,r=0,0
        maxm=0
        mydict=defaultdict(int)
        while r<len(s):
            mydict[s[r]]+=1
            maxm_freq=max(mydict.values())
            
            length=r-l+1
            if length-maxm_freq>k:
                mydict[s[l]]-=1
                l+=1
            maxm=max(maxm,r-l+1)
            r+=1
            
        return maxm
                



