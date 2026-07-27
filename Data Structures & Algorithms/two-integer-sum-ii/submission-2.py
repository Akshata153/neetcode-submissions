class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dt=defaultdict(int)
        j=0
        for i,num in enumerate(numbers):
            temp=target-num
            if temp in dt:
                j=dt[temp]
                return [j+1,i+1]
            dt[num]=i

        return [0,0]

