import sys

class TripletSumCloseToTarget:
  def __init__(self) -> None:
      self.min_diff = sys.maxsize
      self.sum = 0

  def triplet_sum_close_to_target(self, arr, target_sum):
    arr.sort()
    for i in range(0, len(arr) - 1):
      self.search_pair(arr, arr[i], i + 1, target_sum)
    return self.sum


  def search_pair(self, arr, first, start_idx, target_sum) -> int:
    l, r = start_idx, len(arr) - 1

    while l < r:
      if abs(target_sum - first - arr[l] - arr[r]) < self.min_diff:
        self.min_diff = abs(target_sum - first - arr[l] - arr[r])
        self.sum = first + arr[l] + arr[r]

      if arr[l] + arr[r] == target_sum - first:
        break
      elif arr[l] + arr[r] < target_sum - first:
        l += 1
      else:
        r -= 1


def main():
  print(TripletSumCloseToTarget().triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(TripletSumCloseToTarget().triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(TripletSumCloseToTarget().triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()