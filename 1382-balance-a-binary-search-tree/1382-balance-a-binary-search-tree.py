# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_traversal(self, root):
        if not root.left and not root.right:
            return [root.val]
        ans = []
        if root.left:
            ans.extend(self.inorder_traversal(root.left))
        ans.append(root.val)
        if root.right:
            ans.extend(self.inorder_traversal(root.right))
        return ans
    
    def build_bst(self, arr):
        if len(arr) == 1:
            return TreeNode(arr[0])
        n = len(arr)
        mid = n//2
        root = TreeNode(arr[mid])
        root.left = self.build_bst(arr[:mid])
        if mid + 1 < n:
            root.right = self.build_bst(arr[mid + 1:])
        return root

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = self.inorder_traversal(root)
        return self.build_bst(arr)