class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp=[0]*26
        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            temp[ord(s[i])-ord('a')]+=1
            temp[ord(t[i])-ord('a')]-=1

        for x in temp:
            if x!=0:
                return False
        return True