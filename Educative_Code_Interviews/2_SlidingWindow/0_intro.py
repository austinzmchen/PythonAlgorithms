# Statement
#
# Given an array of integers nums, and an integer k, 
#   return the maximum average of a contiguous subarray of length k.


def find_averages_of_subarrays(K, arr):
  result = []
  windowSum, windowStart = 0.0, 0
  for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if windowEnd >= K - 1:
      result.append(windowSum / K)  # calculate the average
      windowSum -= arr[windowStart]  # subtract the element going out
      windowStart += 1  # slide the window ahead

  return result

def find_averages_of_subarrays2(K, arr):
    res = []
    win_sum = 0

    for win_end, v in enumerate(arr):
        win_sum += v
        if win_end >= K - 1:
            res.append(win_sum / K)
            
        if win_end >= K:
            win_sum -= arr[win_end - K]

    return res


def main():
  result = find_averages_of_subarrays2(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
