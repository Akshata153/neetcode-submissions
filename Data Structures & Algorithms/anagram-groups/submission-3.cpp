class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>> mmap;
        for(auto str:strs)
        {
            vector<int> count(26,0);
            for(auto s : str)
            {
                count[s-'a']++;
            }
            string key;
            for (int n :count)
            {
                key+='#'+to_string(n);
            }
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
