class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1=Counter(s1)
        l=0
        dict2=defaultdict(int)
        for r in range(len(s2)):
            dict2[s2[r]]+=1
            if(r-l+1)>len(s1):
                dict2[s2[l]]-=1
                if dict2[s2[l]]==0:
                    del dict2[s2[l]]
                l+=1
            # print(dict2)

            if dict1==dict2:
                return True
        return False