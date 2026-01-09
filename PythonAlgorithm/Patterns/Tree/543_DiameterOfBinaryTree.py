class Solution543:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def recur(node):
            if not node:
                return 0

            left = recur(node.left)
            right = recur(node.right)

            nonlocal res
            res = max(res, left + right + 1)

            return max(left, right) + 1

        recur(root)
        return res - 1