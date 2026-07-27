# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        
        if p == None and q or p and q== None:
            return False
        
        if p and q and p.val!=q.val:
            return False

        lflag=self.isSameTree(p.left,q.left)
        rflag=self.isSameTree(p.right,q.right)

        return lflag and rflag 
