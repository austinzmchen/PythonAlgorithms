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
    winSum = 0

    for winEnd in range(len(arr)):
        winSum += arr[winEnd]
        if winEnd >= K:
            winSum -= arr[winEnd - K]

        if winEnd >= K - 1:
            res.append(winSum / K)

    return res


def main():
  result = find_averages_of_subarrays2(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()
