# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recur(root, left_bound, right_bound):
            if root is None:
                return True
            if root.val >= right_bound or root.val <= left_bound:
                return False
            return recur(root.left, left_bound, root.val) and \
                recur(root.right, root.val, right_bound)
        #
        import sys
        return recur(root, -sys.maxsize-1, sys.maxsize)