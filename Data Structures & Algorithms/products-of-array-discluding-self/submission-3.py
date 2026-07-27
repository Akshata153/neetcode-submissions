class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=1
        s=[0]*len(nums)
        p=[]
        res=[]
        for i in range(len(nums)):
            if i==0: 
                p.append(1)
            else:
                x=x*nums[i-1]
                p.append(x)
        x=1
        for i in range(len(nums)-1,-1,-1):
            
            if i==len(nums)-1: 
                s[i]=1
            else:
                x=x*nums[i+1]
                s[i]=x 
        
        for i in range(len(nums)):
            res.append(p[i]*s[i])
        return res
                