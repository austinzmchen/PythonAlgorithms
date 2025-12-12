# Problem Statement #
# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.

# Example 1:

# Input: [7, 3, 5, 8, 5, 3, 3], and K=2
# Output: 3
# Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have
# to skip 5 because it is not distinct and occurred twice.
# Another solution could be to remove one instance of '5' and '3' each to be left with three
# distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.
# Example 2:

# Input: [3, 5, 12, 11, 12], and K=3
# Output: 2
# Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then
# we can delete any two numbers which will leave us 2 distinct numbers in the result.
# Example 3:

# Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
# Output: 3
# Explanation: We can remove one occurrence of '4' to get three distinct numbers.


# Solution #
# This problem follows the Top ‘K’ Numbers pattern, and shares similarities with Top ‘K’ Frequent Numbers.

# We can following a similar approach as discussed in Top ‘K’ Frequent Numbers problem:

# First, we will find the frequencies of all the numbers.
# Then, push all numbers that are not distinct (i.e., have a frequency higher than one) in a Min Heap based on their frequencies. At the same time, we will keep a running count of all the distinct numbers.
# Following a greedy approach, in a stepwise fashion, we will remove the least frequent number from the heap (i.e., the top element of the min-heap), and try to make it distinct. We will see if we can remove all occurrences of a number except one. If we can, we will increment our running count of distinct numbers. We have to also keep a count of how many removals we have done.
# If after removing elements from the heap, we are still left with some deletions, we have to remove some distinct elements.
 
from heapq import heappop, heappush

def find_maximum_distinct_elements(nums, k):
  freq_dict = {}
  for n in nums:
    freq_dict[n] = freq_dict.setdefault(n, 0) + 1

  distincts = 0
  min_heap = []

  for n, freq in freq_dict.items():
    if freq == 1:
      distincts += 1
    else:
      heappush(min_heap, (freq, n))

  while min_heap and k > 0: # also stop when k is 0
    freq, n = heappop(min_heap)
    if k >= freq - 1:
      distincts += 1
    
    k -= freq - 1 # still need to used up the remaining k, thus k could be negative

  return distincts - max(k, 0)


def main():
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))

main()