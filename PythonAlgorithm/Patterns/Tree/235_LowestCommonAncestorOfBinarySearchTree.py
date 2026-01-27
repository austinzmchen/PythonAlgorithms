# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        def recur(node):
            if not node:
                return False
            
            l = recur(node.left)
            r = recur(node.right)
            
            nonlocal res
            found_both = (l and r) or \
                         ((l or r) and node.val in [p.val, q.val])
            
            if found_both:
                if not res:
                    res = node
            
            return l or r or node.val in [p.val, q.val]
        
        recur(root)
        return res
    