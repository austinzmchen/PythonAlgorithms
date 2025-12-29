# Problem Statement
# Given an integer n, return:
#
# The number of structurally unique BSTs that can be formed with values 1 to n
# (Variation) All the structurally unique BSTs themselves
#
# Example 1:
# Input: n = 3
# Output: 5
#
# The 5 unique BSTs are:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
# Example 3:
# Input: n = 2
# Output: 2
#
#    1      2
#     \    /
#      2  1

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# Dynamic programming approach
def find_unique_trees_1(n) -> int:
  # recur with start value and end value
  return len(recur(1, n))


def recur(start, end) -> list:
  if start > end:
    return [None] # need this to make the double for-loop work down below, just think about when n is 1

  res = []
  for i in range(start, end+1):
    # let's say i is the value of the current node
    lefts = recur(start, i - 1)
    rights = recur(i + 1, end)

    for left in lefts:
      for right in rights:
        root = TreeNode(i)
        root.left = left
        root.right = right
        res.append(root)
  
  return res


    
def find_unique_trees(n) -> list:
    memo = {}

    def count_structures(num_nodes):
        """Count unique structures for num_nodes using BFS-style exploration."""
        if num_nodes in memo:
            return memo[num_nodes]
        
        if num_nodes <= 1:
            return 1
        
        # State: (nodes_for_left, nodes_for_right)
        total = 0
        
        for left_nodes in range(num_nodes):
            # -1 because discounting current node
            right_nodes = num_nodes - 1 - left_nodes
            
            left_count = count_structures(left_nodes)
            right_count = count_structures(right_nodes)
            
            # multiple because if left has a num of structures and right has b num of structures
            # the result is a * b num of structures
            total += left_count * right_count 
        
        memo[num_nodes] = total
        return total

    return count_structures(n)
    

def main():
  print("Total trees: " + str(find_unique_trees(2)))
  print("Total trees: " + str(find_unique_trees(3)))

main()
