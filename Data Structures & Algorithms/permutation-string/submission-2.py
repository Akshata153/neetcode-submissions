class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1f=[0]*26
        s2f=[0]*26
        for ch in s1:
            s1f[ord(ch)-ord('a')]+=1
        l=0
        for r in range(len(s2)):
            s2f[ord(s2[r])-ord('a')]+=1
            if r-l+1 > len(s1):
                s2f[ord(s2[l])-ord('a')]-=1
                l+=1
            if s1f==s2f:
                return True
        return False
