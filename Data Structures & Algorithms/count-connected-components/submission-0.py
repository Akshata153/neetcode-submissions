class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        map=defaultdict(list)
        flag=0

        for a,b in edges:
            map[a].append(b)
            map[b].append(a)

        def dfs(i,par):
            if i in visited or map[i]==[]:
                return
            
            visited.add(i)
            for n in map[i]:
                if i!=n:
                    dfs(n,i)
            
            return
            

        for i in range(n):
            if i not in visited:
                dfs(i,-1)
                flag+=1
        return flag

