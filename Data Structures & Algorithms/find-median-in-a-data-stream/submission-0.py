class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        l=len(self.arr)//2 # 1 index so line 17 -> -1 to make it 0index
        # print(f"{len(self.arr)}  :: {l}")
        if len(self.arr)%2:
            return float(self.arr[l])
        else:
            return (self.arr[l]+self.arr[l-1])/2
        
        