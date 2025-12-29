"""
K Pairs with Largest Sums

Problem: Given two sorted arrays (ascending order) and an integer K, 
find the K pairs with the largest sums. Each pair consists of one number 
from each array.

Example:
    Input: nums1 = [9, 8, 2], nums2 = [6, 3, 1], k = 3
    Output: [[9,6], [8,6], [9,3]]
    Explanation: Largest sums are: 9+6=15, 8+6=14, 9+3=12
"""

from heapq import heappush, heappop

def find_k_largest_pairs(nums1, nums2, k):
  min_heap = []

  for i1, n1 in enumerate(nums1):
    for i2, n2 in enumerate(nums2):
      # fill k nums to the heap first
      if len(min_heap) < k:
        heappush(min_heap, (n1 + n2, i1, i2))
        continue
      
      # the min heap should keep k largest sum
      if n1 + n2 > min_heap[0][0]:
        heappop(min_heap)
        heappush(min_heap, (n1 + n2, i1, i2))
        
      else:
        # we can break since arrays are sorted
        break

  return [[nums1[i1], nums2[i2]]
          for _, i1, i2 in min_heap]


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))

main()