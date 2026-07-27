class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i in range(len(tokens)):
            # print(tokens[i])
            
            if tokens[i] in ['+','-','*','/']:
                x=stack.pop()
                y=stack.pop()
                if tokens[i]=='+':
                    stack.append(y+x)
                elif tokens[i]=='*':
                    stack.append(y*x)
                elif tokens[i]=='-':
                    stack.append(y-x)
                else:
                    stack.append(int(y/x))
                # print(f"op done:",stack[-1])
            else:
                stack.append(int(tokens[i]))
                # print("push only")
        return stack.pop()
