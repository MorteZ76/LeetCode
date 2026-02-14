# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root :
            depth = 1 + max (self.maxDepth(root.left), self.maxDepth(root.right))
        return depth

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        if root :
            if not (self.isBalanced(root.right) and self.isBalanced(root.left)) :
                balance = False
            difference = abs (self.maxDepth(root.left) - self.maxDepth(root.right))
            if difference > 1 :
                balance = False
        return balance
        