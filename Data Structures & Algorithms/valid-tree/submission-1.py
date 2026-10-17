class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map=defaultdict(list)
        visited=set()

        for i,j in edges:
            map[i].append(j)
            map[j].append(i)
        
        def dfs(n,par):
            if n in visited:
                return False
            if map[n]==n:
                return True
            visited.add(n)
            for i in map[n]:
                if par!=i and not dfs(i,n):
                    return False

            return True


        # for i in range(n):
        #     if not dfs(i,-1):
        #         return False
        if not dfs(0,-1) or len(visited)!=n:
            return False
        return True