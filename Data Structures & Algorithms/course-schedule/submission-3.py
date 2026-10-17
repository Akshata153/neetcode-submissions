class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map: pre:next
        visited=set()
        map=defaultdict(list)

        for [crs,pre] in prerequisites:
            map[pre].append(crs)

        def dfs(crs):
            if crs in visited:
                return False
            if map[crs]==[]:
                return True
            visited.add(crs)

            for nextcrs in map[crs]:
                if not dfs(nextcrs):
                    return False
            visited.remove(crs)

            map[crs]=[]
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            