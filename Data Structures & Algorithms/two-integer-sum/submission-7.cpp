class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> mmap;
        int temp;
        for (int i=0;i<nums.size();i++)
        {
            temp=target-nums[i];
            if(mmap.find(temp)!=mmap.end())
                return {mmap[temp],i};
            mmap[nums[i]]=i;
        }
        return {0,0};
    }
};
