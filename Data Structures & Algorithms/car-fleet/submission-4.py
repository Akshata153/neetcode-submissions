class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pair=[[p,s] for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        y=0
        
        count=0
        for p,s in pair:
            y=(target-p)/s
            stack.append(y)
            
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        # if temp:
        #     count+=1

        return len(stack)