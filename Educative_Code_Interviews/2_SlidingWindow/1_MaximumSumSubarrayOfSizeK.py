# Statement
#
# Given an array of integers nums, and an integer k, 
#   return the maximum sum of a contiguous subarray of length k.


import sys

def max_sub_array_of_size_k(k, arr):
  max_sum = 0
  window_sum = 0

  for i in range(len(arr) - k + 1):
    window_sum = 0
    for j in range(i, i+k):
      window_sum += arr[j]
    max_sum = max(max_sum, window_sum)
  return max_sum


def max_sub_array_of_size_k_2(k, arr):
    max_sum = -sys.maxsize - 1
    win_sum = 0

    for win_end, v in enumerate(arr):
        win_sum += v
        if win_end >= k:
            win_sum -= arr[win_end - k]
            
        if win_end >= k - 1:
            max_sum = max(max_sum, win_sum)

    return max_sum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_2(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_2(2, [2, 3, 4, 1, 5])))


main()
