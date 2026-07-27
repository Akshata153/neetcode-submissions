class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<len(s) and r>-1 and l<r:
            while l<len(s) and not s[l].isalnum():
                l+=1
            while r>-1 and not s[r].isalnum():
                r-=1
            # print("Hi")
            # print(f"{s[l]} {s[r]}")
            if l<r and s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
