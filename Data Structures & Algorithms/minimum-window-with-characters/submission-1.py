
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        have=0
        
        tdict=Counter(t)
        needcount=len(tdict)
        l=0
        res=""
        res_count=float('inf')
        for r,ch in enumerate(s):
            window[ch]=window.get(ch,0)+1

            if window[ch]==tdict[ch]:
                have+=1
            
            while have==needcount:
                if (r-l+1)<res_count:
                    res=s[l:r+1]
                    res_count=r-l+1
                
                window[s[l]]-=1
                if s[l] in tdict and window[s[l]] < tdict[s[l]]:
                    have-=1
                
                
                l+=1
        return res