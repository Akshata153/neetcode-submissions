class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[]

        def dfs(i,curr):
            print(f"{i} : {curr}")
            if i>=len(s):
                res.append(curr.copy())
                return
            
            for j in range(i,len(s)):
                if self.ispal(s,i,j):
                    curr.append(s[i:j+1])
                    dfs(j+1,curr)
                    curr.pop()
        dfs(0,[])
        return res

    def ispal(self,s,i,j):
        while i<j:
            if s[i]!=s[j]:
                return False
            i,j=i+1,j-1
            
        return True