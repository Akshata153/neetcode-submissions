class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp=defaultdict(int)
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            temp[s[i]]+=1
            temp[t[i]]-=1

        for x in temp.values():
            if x!=0:
                return False
        return True

            

        