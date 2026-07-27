class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        tot=0
        while n!=1:
            tot=0
            while n!=0:
                tot+=pow((n%10),2)
                n=n//10
            n=tot
            if tot in seen:
                
                return False
            seen.add(tot)
        return True

