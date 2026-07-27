class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            # print(s[i])
            if s[i] in ['(','{','[']:
                stack.append(s[i])
                # print(stack)
                continue
            else:
                if stack:
                    x=stack.pop()
                    # print("pop: ",x)
                    if s[i]==')' and x!='(' or s[i]=='}' and x!='{' or s[i]==']' and x!='[':
                        return False
                else:
                    return False
        if stack:
            return False
            
        return True
