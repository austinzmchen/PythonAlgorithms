class Solution543:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root) -> int:
        if root == None:
            return 0
        #
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        #
        if left + right > self.res:
            self.res = left + right
        #
        return max(left, right) + 1