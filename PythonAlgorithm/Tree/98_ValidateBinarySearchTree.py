# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    
    def isValidBST_1(self, root: Optional[TreeNode]) -> bool:
        def recur(root, left_bound, right_bound):
            if root is None:
                return True
            if root.val >= right_bound or root.val <= left_bound:
                return False
            
            return recur(root.left, left_bound, root.val) and \
                recur(root.right, root.val, right_bound)

        import sys
        return recur(root, -sys.maxsize-1, sys.maxsize)
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        
        return self.isValidBST(root.left) and \
                self.isValidBST(root.right)