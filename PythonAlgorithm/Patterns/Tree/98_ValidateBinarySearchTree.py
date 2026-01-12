# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isValidBST_1(self, root: Optional[TreeNode]) -> bool:
        import sys

        def recur(node, low, high):
            if not node:
                return True

            if low < node.val < high:
                pass
            else:
                return False

            return recur(node.left, low, node.val) and recur(node.right, node.val, high)

        return recur(root, -sys.maxsize-1, sys.maxsize)