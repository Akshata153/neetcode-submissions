class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mymap=Counter(nums)
        arr=[]
        #key, freq
        nums.sort(key=lambda x:(mymap[x],-x))
        # each elemnet of nums parsed and looked into its scoring tupple  (freq, -key)and is sorted using score
        # print(nums)
        return nums