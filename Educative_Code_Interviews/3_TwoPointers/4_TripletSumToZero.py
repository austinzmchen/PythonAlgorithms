def search_triplets(arr):
  arr.sort()
  triplets = []
  for i in range(0, len(arr) - 1):
    search_pair(arr, -arr[i], i + 1, triplets)

  return triplets


def search_pair(arr, target, start_idx, triplets):
  left, right = start_idx, len(arr) - 1
  while left < right:
    if arr[left] + arr[right] == target:
      triplets.append([-target, arr[left], arr[right]])
      left += 1
      right -= 1
    elif arr[left] + arr[right] < target:
      left += 1
    else:
      right -= 1


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()