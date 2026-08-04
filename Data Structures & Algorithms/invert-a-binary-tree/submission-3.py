# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def func(n):
            if n is None:
                return 
            
            func(n.left)
            func(n.right)
            n.left,n.right=n.right,n.left
            return

        func(root)
        return root