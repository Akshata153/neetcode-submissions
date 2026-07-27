class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        # m=0
        
        sortedkeys=sorted(count,key=lambda x:count[x],reverse=True)
        # print(lambda x:count[x])

        return sortedkeys[:k]

        
        # return [n for c,n in heap]