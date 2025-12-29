# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        _deque = deque()
        _deque.append(root)
        results = []
        #
        while len(_deque) > 0:
            size = len(_deque)
            ls = []
            for _ in range(size):
                n = _deque.popleft()
                if n.left:
                    _deque.append(n.left)
                if n.right:
                    _deque.append(n.right)
                ls.append(n.val)
            results.append(ls)
        #
        return results[::-1]