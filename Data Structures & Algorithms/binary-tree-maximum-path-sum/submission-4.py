# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxm=float('-inf')

        def dfs(node):
            if not node:
                return 0

            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            self.maxm=max(self.maxm,left+right+node.val)
            # print(self.maxm)
            a=max(left,right)+node.val
            return max(a,node.val)
        es=dfs(root)
        # print(es)
        self.maxm=max(self.maxm,es)
        return self.maxm