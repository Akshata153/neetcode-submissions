class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            map1=defaultdict(int)
            for ch in s:
                map1[ch]+=1
            res[tuple(sorted(map1.items()))].append(s)
        return list(res.values())