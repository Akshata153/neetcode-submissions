# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q=[]
        node=root
        q.append(root)
        while q:
            while node:
                q.append(node)
                node=node.left
            
            x=q.pop()
            k-=1
            if k==0:
                return x.val
            node=x.right
        return 0
