class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt=defaultdict(list)

        for s in strs:
            sorted_word=tuple(sorted(s))
            dt[sorted_word].append(s)

        return list(dt.values())