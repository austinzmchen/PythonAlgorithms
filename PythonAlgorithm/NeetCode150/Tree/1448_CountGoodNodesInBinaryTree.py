
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def recur(node, curr_max):
            if not node:
                return 0

            c = 0
            if node.val >= curr_max:
                c = 1
            curr_max = max(curr_max, node.val)

            return c + \
                recur(node.left, curr_max) + \
                recur(node.right, curr_max)
        
        return recur(root, root.val)