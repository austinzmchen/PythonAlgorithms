# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def recur(node, depth):
            if not node:
                return
            
            # pre-order to add the node
            if len(res) < depth + 1:
                res.append(node.val)

            recur(node.left, depth + 1)
            recur(node.right, depth + 1)

            # post-order to re-write the node
            if depth < len(res):
                res[depth] = node.val

        recur(root, 0)
        return res
    

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        from collections import deque
        queue = deque()
        queue.append(root)

        res = []
        while queue:
            size = len(queue)
            for i in range(size):
                n = queue.popleft()
                if i == size - 1:
                    res.append(n.val)

                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

        return res