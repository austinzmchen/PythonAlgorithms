# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
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
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a, b):
            if not a or not b:
                return a == b
            
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

        def recur(n1, n2):
            if not n2:
                return True
            if not n1:
                return False
        
            return same(n1, n2) or recur(n1.left, n2) or recur(n1.right, n2)
        
        return recur(root, subRoot)