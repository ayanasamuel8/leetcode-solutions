# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestNode(self, root, depth):
        if not root.left and not root.right:
            return root, depth
        
        left = right = None
        leftVal = rightVal = 0
        if root.left:
            left, leftVal = self.deepestNode(root.left, depth + 1)
        if root.right:
            right, rightVal = self.deepestNode(root.right, depth + 1)
        if leftVal > rightVal:
            return left, leftVal
        if rightVal > leftVal:
            return right, rightVal
        return root, leftVal

    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans, val = self.deepestNode(root, 0)
        return ans