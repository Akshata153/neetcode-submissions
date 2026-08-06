# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or self.same(p.val,q.val)==-1:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    def same(self,a,b):
            if a!=b:
                return -1
            return 0

