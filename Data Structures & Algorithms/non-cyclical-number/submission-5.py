class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        sum=0
        while n!=1:
            
            while n>0:
                sum+=pow(n%10,2)
                n=n//10
            # print(sum)
            # print("visited: ",visited)
            if sum==1:
                return True
            if sum in visited:
                return False
            visited.add(sum)
            n=sum
            sum=0
        # print("Hi")
        return True
        