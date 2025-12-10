# connect the nodes on the same level to a linked list using `next`

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
  if not root:
    return []

  deq = deque()
  deq.append(root)
  prev = None

  while deq:
    length = len(deq)

    for _ in range(length):
      node = deq.popleft()
      
      if node.left:
        deq.append(node.left)
      if node.right:
        deq.append(node.right)
      
      if prev:
        prev.next = node
      prev = node
    #   
    prev = None
  #
  return root


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()
