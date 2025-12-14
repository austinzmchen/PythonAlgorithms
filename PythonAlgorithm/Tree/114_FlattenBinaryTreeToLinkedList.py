# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        #
        left_n = root.left
        right_n = root.right
        #
        if left_end := self.flatten(root.left):
            left_end.right = right_n
            root.right = left_n
        #
        root.left = None
        right_end = self.flatten(root.right)
        return right_end or left_end or root