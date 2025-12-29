class Solution236:
    def __init__(self):
        self.res = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.res
    
    def dfs(self, root, p, q) -> int:
        if not root:
            return 0
        #
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        #
        count = left + right
        if root == p or root == q:
            count += 1
        if count == 2 and not self.res:
            self.res = root
        return count
      
      
class Solution236_2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
    
    def dfs(self, root, p, q):
        if not root:
            return None
        #
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        #
        if left and right:
            return root
        if root == p or root == q:
            return root
        return left if left else right