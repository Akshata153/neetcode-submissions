class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for j in range(n+1):
            count=0
            i=j
            while i:
                i=i&i-1
                count+=1
            # print(f"{i} {count}")
            res.append(count)
        return res