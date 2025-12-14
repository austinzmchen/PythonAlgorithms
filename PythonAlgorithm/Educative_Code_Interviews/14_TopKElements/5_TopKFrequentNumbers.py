from heapq import heappop, heappush

def find_k_frequent_numbers(nums, k):
  freq_dict = {}
  for n in nums:
    freq_dict[n] = freq_dict.setdefault(n, 0) + 1

  min_heap = []
  for num, freq in freq_dict.items():
    if len(min_heap) < k:
      heappush(min_heap, (freq, num))
    else:
      if freq > min_heap[0][0]:
        heappop(min_heap)
        heappush(min_heap, (freq, num))

  return [t[1] for t in min_heap]


def main():
  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))
  print("Here are the K frequent numbers: " +
        str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))

main()