# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        dummy = TreeNode()
        dummy.next = head
        fast = head
        slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None
        right = middle.next
        root = TreeNode(middle.val, self.sortedListToBST(head), self.sortedListToBST(right))
        return root
