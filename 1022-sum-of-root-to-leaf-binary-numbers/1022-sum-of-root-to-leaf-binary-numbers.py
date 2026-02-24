# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def listOfNumbers(self, root, val):
        if not root.left and not root.right:
            self.ans += (val << 1 | root.val)
        if root.left:
            self.listOfNumbers(root.left, val << 1 | root.val)
        if root.right:
            self.listOfNumbers(root.right, val << 1 | root.val)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.listOfNumbers(root, 0)
        return self.ans