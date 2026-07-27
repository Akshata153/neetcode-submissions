class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict=defaultdict(int)
        for n in nums:
            mydict[n]+=1
        arr=sorted(mydict,key=lambda x:mydict[x],reverse=True)
        return arr[:k]
