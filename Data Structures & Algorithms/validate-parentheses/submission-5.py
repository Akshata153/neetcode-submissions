class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if  len(s)%2:
            return False
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                if s[i]==")" and stack.pop()!="(" or s[i]=="}" and stack.pop()!="{" or s[i]=="]" and stack.pop()!="[":
                    return False
        if len(stack):
            return False
        return True 
            