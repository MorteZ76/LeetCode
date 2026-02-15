# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_depths = {}
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            max_depths[root] = 0
            return 0
        r = 0
        l = 0
        if root.left :
            l = self.maxDepth(root.left) + 1
        if root.right :
            r = self.maxDepth(root.right) + 1
        self.max_depths[root] = max(l,r)
        return max(l,r)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root : 
            return 0
        tmp = self.maxDepth(root)
        current_diameter = 0 
        max_diameter = 0
        left_max = 0
        right_max = 0
        if root.left : 
            current_diameter += self.max_depths[root.left] + 1
            left_max = self.diameterOfBinaryTree(root.left)
            max_diameter = max(max_diameter, left_max)
        if root.right : 
            current_diameter += self.max_depths[root.right] + 1
            right_max = self.diameterOfBinaryTree(root.right)
            max_diameter = max(max_diameter, right_max)
        max_diameter = max(max_diameter, current_diameter)
        return max_diameter