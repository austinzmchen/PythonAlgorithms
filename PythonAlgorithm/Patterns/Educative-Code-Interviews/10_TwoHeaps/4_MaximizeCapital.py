# You are given:

# k: Maximum number of projects you can complete
# w: Initial capital
# profits[]: Array of profits for each project
# capital[]: Array of minimum capital required to start each project

# Goal: Maximize your capital by selecting at most k distinct projects.

# Example 1:
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4

# Explanation:
# - Start with capital = 0
# - Do project 0 (requires 0, profit = 1) → capital = 1
# - Do project 2 (requires 1, profit = 3) → capital = 4
#
# Example 2:
# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6

# Explanation:
# - Do project 0 (requires 0, profit = 1) → capital = 1
# - Do project 1 (requires 1, profit = 2) → capital = 3
# - Do project 2 (requires 2, profit = 3) → capital = 6
#

from heapq import heappop, heappush

# Strategy:
# - Use min heap to store projects by capital requirement
# - Use max heap to store available (affordable) projects by profit
# - Greedily select the most profitable available project

def find_maximum_capital(capitals, profits, k, w):
  # use min heap to find the minimum cap requirement proj
  min_heap = []
  for i, c in enumerate(capitals):
    heappush(min_heap, (c, i))

  max_heap_profits = []
  res = w

  for _ in range(k):
    while min_heap and min_heap[0][0] <= res:
      # these are the projs we can do, but which are the most profitable
      capital, idx = heappop(min_heap)
      heappush(max_heap_profits, -profits[idx])

    # If no projects are affordable, we're done
    if not max_heap_profits:
        break
    
    # do this proj
    res += -heappop(max_heap_profits)
  #
  return res


def main():
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))

main()
