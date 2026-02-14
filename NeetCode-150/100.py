# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same = True
        if (p  and (not q) ) or ( (not p) and q) :
            is_same = False
        if (p and q) :
            if p.val != q.val :
                is_same = False
            if self.isSameTree(p.left, q.left) == False or self.isSameTree(p.right, q.right) == False :
                is_same = False
        return is_same
