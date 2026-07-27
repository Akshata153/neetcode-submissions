class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        if  len(s)%2:
            return False

        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{' :
                stack.append(s[i])
            else:
                if not len(stack): #stack.empty()
                    return False
                if s[i]==')'and stack.pop() != '(' or s[i]==']'and stack.pop() != '[' or s[i]=='}'and stack.pop() != '{':
                    return False

        if len(stack):
            return False
        return True

