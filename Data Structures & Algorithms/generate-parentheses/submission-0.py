class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        def back(curr:str, opencount:int, closedcount:int):
            if len(curr)==2*n:
                #got current string
                res.append(curr)
            
            if opencount<n:
                #can add open bracket
                back(curr+"(",opencount+1,closedcount)
            if closedcount<opencount:
                #can add closed baracket
                back(curr+")",opencount,closedcount+1)

        back("",0,0)
        return res