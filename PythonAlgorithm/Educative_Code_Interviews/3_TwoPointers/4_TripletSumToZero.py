# /*
# Problem Statement #
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:
# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.

# Example 2:
# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.
#  */

def search_triplets_1(arr):
  arr.sort()
  triplets = []
  for i in range(0, len(arr) - 2):
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


def search_triplets(arr):
  arr.sort()
  res = []

  def search_pair(target, start_idx):
    left, right = start_idx, len(arr) - 1
    while left < right:
      if arr[left] + arr[right] == target:
        res.append([-target, arr[left], arr[right]])
        left += 1
        right -= 1
      elif arr[left] + arr[right] < target:
        left += 1
      else:
        right -= 1

  for i in range(0, len(arr) - 2):
    search_pair(-arr[i], i + 1)
  return res


def main():
  print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
  print(search_triplets([-5, 2, -1, -2, 3]))


main()