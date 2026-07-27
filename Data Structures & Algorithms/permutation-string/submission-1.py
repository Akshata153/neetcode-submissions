class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict=Counter(s1)
        s2dict=Counter(s2[0:len(s1)])
        if s1dict==s2dict:
            return True
        for i in range(len(s1),len(s2)):
            s2dict[s2[i]]+=1
            s2dict[s2[i-len(s1)]]-=1
            if s2dict[s2[i-len(s1)]]==0:
                del s2dict[s2[i-len(s1)]]
            if s1dict==s2dict:
                return True
        return False
