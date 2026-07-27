class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mmap=defaultdict(int)
        if len(s) !=len(t):
            return False
        for i in range(len(s)):
            mmap[s[i]]+=1
            mmap[t[i]]-=1
        for i in range(len(s)):
            if mmap[s[i]]!=0:
                return False
            
        return True