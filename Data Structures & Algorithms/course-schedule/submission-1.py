class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited=set()
        map=defaultdict(list)
        for [crs,pre] in prerequisites:
            map[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if map[crs] is None:
                return True
            visited.add(crs)
            for x in map[crs]:
                if not dfs(x):
                    return False
                    
            visited.remove(crs)
            map[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        




