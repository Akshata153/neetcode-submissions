# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            a=dfs(node.left)
            b=dfs(node.right)
            if a==-1 or b==-1:
                return -1
            if abs(a-b)>1:
                return -1
            return 1+(max(a,b))

        return dfs(root)!=-1
        
