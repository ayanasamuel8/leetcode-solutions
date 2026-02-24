# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def listOfNumbers(self, root):
        if not root.left and not root.right:
            return [[root.val, 1]]
        ans = []
        if root.left:
            ret = self.listOfNumbers(root.left)
            for i in range(len(ret)):
                new = root.val << ret[i][1]
                ret[i] = [new | ret[i][0], ret[i][1] + 1]
            ans.extend(ret)
        if root.right:
            ret = self.listOfNumbers(root.right)
            for i in range(len(ret)):
                new = root.val << ret[i][1]
                ret[i] = [new | ret[i][0], ret[i][1] + 1]
            ans.extend(ret)
            
        return ans

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        arr = [i[0] for i in self.listOfNumbers(root)]
        return sum(arr)