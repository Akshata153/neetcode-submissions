class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_map={chr(i):0 for i in range(ord('a'),ord('z')+1)}

        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            alpha_map[s[i]]+=1
            alpha_map[t[i]]-=1
        for val in alpha_map.values():
            if val!=0:
                return False
        return True
