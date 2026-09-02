class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        count=Counter(tasks)
        maxheap=[]
        for i in count.values():
            heapq.heappush(maxheap,-i)
    
        q=[]

        while maxheap or q:
            time+=1
            if not maxheap:
                time=q[0][1]
            else:
                x=heapq.heappop(maxheap)+1
                if x:
                    q.append([x,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.pop(0)[0])

        return time

