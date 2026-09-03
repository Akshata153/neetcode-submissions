class MedianFinder:

    def __init__(self):
        self.small=[] #max heap
        self.large=[] #minheap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)

        #check if largest in small <= smallest in large
        if self.small and self.large and -self.small[0]>self.large[0]:
            x=heapq.heappop(self.small)
            heapq.heappush(self.large,-x)

        #check difff in len; differ by <=1
        if len(self.small)-len(self.large)>1:
            x=heapq.heappop(self.small)
            heapq.heappush(self.large,-x)
        elif len(self.large)-len(self.small)>1:
            x=heapq.heappop(self.large)
            heapq.heappush(self.small,-x)
        

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return (-self.small[0]+self.large[0])/2
        elif len(self.small)>len(self.large):
            return float(-self.small[0])
        return float(self.large[0])
        
        