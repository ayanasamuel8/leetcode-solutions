# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root):
        if not root.left and not root.right:
            return 1, True
        left = 0
        right = 0
        if root.left:
            left, isbalance = self.depth(root.left)
            if not isbalance:
                return 0, False
        if root.right:
            right, isbalance = self.depth(root.right)
            if not isbalance:
                return 0, False
        diff = left - right
        if diff not in [-1, 0, 1]:
            return 0, False
        return max(left, right) + 1, True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        left, isbalance = self.depth(root)
        return isbalance