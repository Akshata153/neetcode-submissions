class CountSquares:

    def __init__(self):
        self.map=defaultdict(int)
        self.points=[]

    def add(self, point: List[int]) -> None:
        self.points.append(point)
        x,y=point
        self.map[(x,y)]+=1
        # print(self.map)
        

    def count(self, point: List[int]) -> int:
        px,py=point
        count=0
        for (x,y) in self.points:
            if abs(x-px)!=abs(y-py) or x==px or y==py:
                continue
            count+=(self.map[(x,py)]*self.map[(px,y)])
        return count
            
        
