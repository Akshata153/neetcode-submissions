class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)<2:
            arr[-1]=-1 if len(arr)>0 else None
            return arr
        maxm=arr[-1]
        res=[-1]*len(arr)
        res[-2]=maxm
        for i in range(len(arr)-3,-1,-1):
            if maxm<arr[i+1]:
                maxm=arr[i+1]
            res[i]=maxm
        return res


            