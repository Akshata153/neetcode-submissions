class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mymap = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl","6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz" }
        res=[""]
        for i in digits:
            temp=[]
            # print("res ",res)
            for curr in res:
                for c in mymap[i]:
                    
                    temp.append(curr+c)
                    # print("temp ",temp)
            res=temp
        return res
