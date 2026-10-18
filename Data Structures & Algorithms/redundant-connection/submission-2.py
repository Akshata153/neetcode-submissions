class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        map=defaultdict(list)
        visited=set()
        def dfs(n,par):
            # print(f"{n} : {par} == {map}")
            if n in visited:
                return True
            
            # visited[n]=True
            visited.add(n)
            for i in map[n]:
                if i!=par and dfs(i,n):
                    return True
            visited.remove(n)
            return False


        
        for a,b in edges:
            map[a].append(b)
            map[b].append(a)
            # visited=[False]*(n+1)
            if dfs(a,-1):
                return [a,b]
        return []