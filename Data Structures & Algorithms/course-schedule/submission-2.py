class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q=deque()
        map=defaultdict(list)
        indeg=[0 for _ in range(numCourses)]
        for [crs,pre] in prerequisites:
            map[pre].append(crs)
            indeg[crs]+=1
        
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)

        while q:
            pre=q.popleft()
            for n in map[pre]:
                indeg[n]-=1
                if indeg[n]==0:
                    q.append(n)
        for i in range(numCourses):
            if indeg[i]!=0:
                return False
        return True


        