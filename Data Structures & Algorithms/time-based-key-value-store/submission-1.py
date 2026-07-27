import bisect
class TimeMap:

    def __init__(self):
        self.hmap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((timestamp,value))
        


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap.keys():
            return ""
        arr=self.hmap[key] #(timestamp,value)
        time=[t for t,_ in arr] # only timestamps
        index=bisect.bisect_right(time,timestamp)-1 #gets equal or prev timestamp
        if index>=0:
            return arr[index][1]
        else:
            return ""


