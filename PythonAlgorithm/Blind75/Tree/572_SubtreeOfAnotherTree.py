# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(a, b):
            if not a or not b:
                return a == b
            
            return a.val == b.val and \
                isSame(a.left, b.left) and \
                isSame(a.right, b.right)

        if not subRoot:
            return True
        if not root:
            return False
        
        return isSame(root, subRoot) or \
                self.isSubtree(root.left, subRoot) or \
                self.isSubtree(root.right, subRoot)
                
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(node, node2):
            if node is None and node2 is None:
                return True
            if node is None or node2 is None:
                return False
            if node.val != node2.val:
                return False
            
            return equal(node.left, node2.left) and equal(node.right, node2.right)

        def recur(node):
            if not node:
                return False

            return equal(node, subRoot) or \
                    recur(node.left) or \
                    recur(node.right)
        
        return recur(root)