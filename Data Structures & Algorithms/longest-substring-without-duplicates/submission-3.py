class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset=deque()
        l,r=0,0
        myset
        count=0
        maxm=0
        while r<len(s):
            # print(myset)
            while s[r] in myset:
                # print("pop",myset[-1])
                myset.popleft()
                # print("pop",)
                count-=1
            myset.append(s[r])
            count+=1
            maxm=max(maxm,count)
            r+=1
        return maxm
        