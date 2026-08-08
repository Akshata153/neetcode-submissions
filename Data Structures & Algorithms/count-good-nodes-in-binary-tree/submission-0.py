# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q=[]
        q.append((root,-float('inf')))
        res=0
        while q:
            n,maxVal=q.pop()
            if n.val>=maxVal:
                res+=1
            if n.left:
                q.append((n.left,max(n.val,maxVal)))
            if n.right:
                q.append((n.right,max(n.val,maxVal)))
        return res
