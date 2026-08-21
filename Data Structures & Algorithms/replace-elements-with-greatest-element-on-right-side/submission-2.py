class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxm=-1

        for i in range(len(arr)-1,-1,-1):
            arr[i],maxm=maxm,max(maxm,arr[i])

        return arr