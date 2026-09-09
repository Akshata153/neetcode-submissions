class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,curr=[],[]

        def dfs(i):
            if i>=len(s):
                res.append(curr.copy())
                return
            print("call:",curr)
            for j in range(i,len(s)):
                # print(f"{i},{j}")
                if self.isPali(s,i,j):
                    
                    curr.append(s[i:j+1])
                    # print(f"{i}:{j} : {curr}")
                    dfs(j+1)
                    curr.pop()
                    # print(f"pop {i}:{j} : {curr}")
        dfs(0)
        return res

    def isPali(self,s,l,r):
        while l<r:
            if s[l]!=s[r]:
                return False
            l,r=l+1,r-1
        return True
                