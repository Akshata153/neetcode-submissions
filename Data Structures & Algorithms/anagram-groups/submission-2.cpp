class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>> mmap;
        for(auto str:strs)
        {
            string key=str;
            sort(key.begin(),key.end());
            mmap[key].push_back(str);
        }
        vector<vector<string>> result;
        for(auto pair:mmap)
        {
            result.push_back(pair.second);
        }
        return result;
    }
};
