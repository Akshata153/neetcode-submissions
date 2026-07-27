class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFFF
        max_mask=0x7FFFFFFF
        while b!=0:
            temp=((a&b)<<1)&mask
            a=(a^b)&mask
            b=temp
        return a if a<=max_mask else ~(a ^ mask)