class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        arr=self.hashmap[key]
        if not arr:
            return ""
        arr.sort()
        # print(arr)
        l,r=0,len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m][0]==timestamp:
                # print(arr[m][1])
                return arr[m][1]
            elif arr[m][0]<timestamp:
                l=m+1
            else:
                r=m-1
        return arr[l-1][1] if arr[l-1][0]<=timestamp else ""
                

        
