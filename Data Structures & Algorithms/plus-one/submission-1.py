class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        carry=1
        for i in range(len(digits)-1,-1,-1):
            # print(digits)
            if digits[i]==9:
                carry=1
                digits[i]=0
            else:
                digits[i]+=carry
                carry=0
                break
        if carry:
            
            res=[0]*(len(digits))
            # print(res)
            res[0]=carry
            # print(res)
            res[1:len(digits)]=digits
            return res
        return digits
            
