class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg=[0*n for n in range(numCourses)]
        map=defaultdict(list)
        q=deque()

        for [crs,prev] in prerequisites:
            map[prev].append(crs)
            indeg[crs]+=1
        res=[]
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        flag=0
        while q:
            # print(q)
            n=q.popleft()
            res.append(n)
            flag+=1
            for i in map[n]:
                indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
        return res if flag==numCourses else []
