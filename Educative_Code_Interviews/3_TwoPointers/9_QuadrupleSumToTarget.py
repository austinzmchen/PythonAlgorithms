def search_quadruplets(arr, target):
  quadruplets = []
  arr.sort()

  for i in range(len(arr) - 3):
    if i > 0 and arr[i] == arr[i - 1]:
      continue
    for j in range(i + 1, len(arr) - 2):
      if j > i + 1 and arr[j] == arr[j - 1]:
        continue
      pair_with_targetsum(arr, target, j + 1, arr[i], arr[j], quadruplets)

  return quadruplets


def pair_with_targetsum(arr, target_sum, start_idx, first, second, quadruplets):
  start, end = start_idx, len(arr) - 1
  while start < end:
    sum = first + second + arr[start] + arr[end]
    if sum == target_sum:
      quadruplets.append([first, second, arr[start], arr[end]])
      start += 1
      end -= 1
      while start < end and arr[start] == arr[start - 1]:
        start += 1
      while end > start and arr[end] == arr[end + 1]:
        end -= 1

    elif sum < target_sum:
      start += 1
    else:
      end -= 1


def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
