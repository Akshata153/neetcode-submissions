class Solution:
    def myPow(self, x: float, n: int) -> float:
        product=1.0
        while n:
            if n>=0:
                product=product*x
                n-=1
            else:
                product=product/x
                n+=1
            
        return product