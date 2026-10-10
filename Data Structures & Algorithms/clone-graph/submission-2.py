"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map={}
        if not node:
            return 

        def dfs(n):
            if n in map:
                return map[n]
            temp=Node(n.val)
            map[n]=temp
            for neigh in n.neighbors:
                temp.neighbors.append(dfs(neigh))
            return temp
        return dfs(node)
       


