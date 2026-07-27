class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int> mmap;
        if (s.length()!=t.length())
            return false;
        for(int i=0;i<s.length();i++)
        {
            mmap[s[i]]+=1;
            mmap[t[i]]-=1;
        }
        for(int i=0;i<s.length();i++)
        {
            if (mmap[s[i]]!=0)
                return false;
        }
        return true;
    }
};
