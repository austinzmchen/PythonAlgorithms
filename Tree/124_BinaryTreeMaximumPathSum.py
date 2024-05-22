# Definition for a binary tree node.

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        import sys
        _max = -sys.maxsize-1
        def recur(node):
            if not node:
                return 0
            left = recur(node.left)
            right = recur(node.right)
            nonlocal _max
            _max = max(_max, 
                       left + right + node.val, 
                       left + node.val,
                       right + node.val,
                       node.val)
            #
            return max(left + node.val, 
                       right + node.val, 
                       node.val)
        #
        recur(root)
        return _max
      
      
    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        import sys
        _max = -sys.maxsize-1
        def recur(node):
            if not node:
                return 0
            #
            nonlocal _max
            left = recur(node.left)
            right = recur(node.right)
            _max = max(_max, 
                       node.val,
                       left + node.val,
                       right + node.val,
                       left + right + node.val)
            
            return max(max(left, right) + node.val, node.val)
        #
        recur(root)
        return _max