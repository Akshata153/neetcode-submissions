class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict=defaultdict(int)
        for n in nums:
            my_dict[n]+=1
            
        sorted_keys=sorted(my_dict,key=lambda x:my_dict[x],reverse=True)
        return sorted_keys[:k]
