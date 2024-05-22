
import math


def smallest_subarray_with_given_sum(s, arr):
  minLen = math.inf
  sum = 0
  winStart = 0

  for winEnd in range(len(arr)):
    sum += arr[winEnd] 
    while sum >= s and winEnd >= winStart:
      minLen = min(minLen, winEnd - winStart + 1)
      sum -= arr[winStart]
      winStart += 1
      
  if minLen == math.inf: return 0
  return minLen

def main():
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
  print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()