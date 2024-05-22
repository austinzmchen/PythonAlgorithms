from heapq import heappush, heappop


def find_k_largest_pairs(nums1, nums2, k):
  min_heap = []

  for i1, n1 in enumerate(nums1):
    for i2, n2 in enumerate(nums2):
      if len(min_heap) < k:
        heappush(min_heap, (n1 + n2, i1, i2))
      else:
        if n1 + n2 > min_heap[0][0]:
          heappop(min_heap)
          heappush(min_heap, (n1 + n2, i1, i2))
        else:
          break

  return [[nums1[i1], nums2[i2]] for _, i1, i2 in min_heap]


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()
