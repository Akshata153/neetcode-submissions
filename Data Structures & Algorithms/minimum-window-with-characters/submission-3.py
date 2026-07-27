class Solution:
    def minWindow(self, t: str, s: str) -> str:
        dict1=Counter(s)
        dict2=defaultdict(int)
        l,have=0,0
        need=len(s)
        minm=float('inf')
        res=""
        for r in range(len(t)):
            
            dict2[t[r]]+=1
            # print(dict2)
            if dict1[t[r]]>=dict2[t[r]]:
                have+=1
                # print("have: ",t[r])
                # print(have)

            while need==have:
                # print("need==have")
                if minm>(r-l+1):
                    minm=min(minm,r-l+1)
                    
                    res=t[l:r+1]
                    # print(res)
                if dict2[t[l]]==dict1[t[l]]:
                    have-=1
                dict2[t[l]]-=1
                l+=1

        # if need==have:
            
        return res