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
    winSum, winStart = 0, 0

    for winEnd in range(len(arr)):
        winSum += arr[winEnd]
        if winEnd >= k - 1:
            max_sum = max(max_sum, winSum)
            winSum -= arr[winStart]

    return max_sum

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_2(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_2(2, [2, 3, 4, 1, 5])))


main()
