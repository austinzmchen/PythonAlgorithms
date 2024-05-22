def length_of_longest_substring(arr, k):
  maxLen = 0
  zeroCount = 0
  winS = 0

  for winE in range(len(arr)):
    if arr[winE] == 0: zeroCount += 1

    while zeroCount > k:
        if arr[winS] == 0:
            zeroCount -= 1
        winS += 1

    maxLen = max(maxLen, winE - winS + 1)

  return maxLen



def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()