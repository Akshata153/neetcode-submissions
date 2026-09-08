class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(curr,opencount,closecount):
            if len(curr)==2*n:
                res.append(curr)

            if opencount<n:
                
                dfs(curr+"(",opencount+1,closecount)
            if closecount<opencount:
                
                dfs(curr+")",opencount,closecount+1)
        dfs("",0,0)
        return res   
        
            