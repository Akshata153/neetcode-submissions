class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                # print(digits)
                digits[i]=digits[i]+carry
                carry=0
                continue
            if carry:    
                digits[i]=0
                carry=1
                continue
            digits[i]
        if carry:
            return [1]+digits
        return digits
        