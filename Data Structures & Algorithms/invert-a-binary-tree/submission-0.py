# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        stack=[root]
        
        

        while stack:
            
            x=stack.pop()
            
            # a,b=swap(x.left,x.right)
            x.left,x.right=x.right,x.left
            if x.left:
                stack.append(x.left)
            if x.right:
                stack.append(x.right)
            
        return root


