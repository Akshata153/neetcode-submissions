class Solution:
    def isHappy(self, n: int) -> bool:
        hmap=defaultdict(int)
        tot=0
        while n!=1:
            tot=0
            while n!=0:
                tot+=pow((n%10),2)
                n=n//10
            n=tot
            if hmap[tot]==1:
                print(tot)
                return False
            hmap[tot]+=1
        return True

