from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if root == None:
    return []

  result = []
  q = deque()
  q.append(root)
  flag = False
  
  while len(q) > 0:
    length = len(q)
    list = []
    for i in range(length):
      node = q.popleft()
      if flag:
        return node
      elif node.val == key:
        flag = True

      list.append(node.val)
      if node.left != None:
        q.append(node.left)
      if node.right != None:
        q.append(node.right)

    result.append(list)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
