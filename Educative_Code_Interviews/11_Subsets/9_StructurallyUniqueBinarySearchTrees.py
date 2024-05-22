
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_unique_trees(n):
  return recur(1, n)


def recur(start, end):
  if start > end:
    return [None] # need this to make the double for-loop work down below, just think about when n is 1

  result = []
  for i in range(start, end+1):
    lefts = recur(start, i - 1)
    rights = recur(i + 1, end)

    for left in lefts:
      for right in rights:
        root = TreeNode(i)
        root.left = left
        root.right = right
        result.append(root)
  
  return result


def main():
  print("Total trees: " + str(len(find_unique_trees(2))))
  print("Total trees: " + str(len(find_unique_trees(3))))


main()
