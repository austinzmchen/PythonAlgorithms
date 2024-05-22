# not tested
from collections import deque


class Solution:
  # The in-order successor of a node is the left-most node in its right sub-tree, if exists. 
  # If not, then it is the root of the smallest left sub-tree this node is in.
  def inorderSuccessor(self, root, p):
    prev = None
    curr = root
    while curr:
      if p.val < curr.val:
        prev = curr
        curr = curr.left
      else: # if equal, still need to proceed to find the smallest left node
        curr = curr.right
    return prev
  
    
  def inorderSuccessor2(self, root, p):
    stack = deque()
    # use a stack
    def recur(root, stack):
      if not root:
        return
      recur(root.left, stack)
      stack.append(root)
      recur(root.right, stack)
    #
    recur(root, stack)
    #
    while len(stack) > 0:
      n = stack.pop()
      if n == p:
        return stack[-1]
    #
    return None
      
