class Solution:
    def isHappy(self, n: int) -> bool:
        hash={}
        while True:
            res=0
            # print(hash)
            while n:
                print(n)
                res+=pow((n%10),2)
                n=n//10
            # print("res",res)
            if res==1:
                return True
            elif res in hash:
                return False
            else:
                n=res
                hash[res]=1
        return False
