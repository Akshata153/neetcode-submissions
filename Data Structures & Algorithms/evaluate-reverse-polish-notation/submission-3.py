class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for i in range(len(tokens)):
            if tokens[i].lstrip('-').isnumeric():
                stack.append(tokens[i])
                
            else:
                num1=int(stack.pop())
                # if len(stack):
                if len(stack):
                    num2=int(stack.pop())
                else:
                    num2=0
                op=tokens[i]
                if op=="+":
                    res=num1+num2
                if op=="-":
                    res=num2-num1
                if op=="*":
                    res=num1*num2
                if op=="/":
                    res=int(num2/num1)
                stack.append(res)
        
        return int(stack.pop())

                
                