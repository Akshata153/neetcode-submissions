class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[[p,s] for p,s in zip(position,speed)]
        stack=[]
        for p,s in sorted(pair)[::-1]:#reverse order
        # we dont know wt speed is front one going , might have slowed so reverse!
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

