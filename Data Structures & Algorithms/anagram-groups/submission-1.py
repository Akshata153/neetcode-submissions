class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for word in strs:
            sortedword=''.join(sorted(word))
            result[sortedword].append(word)

        return list(result.values())
