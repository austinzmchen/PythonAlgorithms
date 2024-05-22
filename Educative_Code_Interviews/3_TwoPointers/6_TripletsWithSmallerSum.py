
class TripletsWithSmallerSum:
  def __init__(self) -> None:
    self.count = 0

  def triplet_with_smaller_sum(self, arr, target):
    arr.sort()
    for i in range(0, len(arr) - 1):
      self.search_pair(arr, arr[i], i + 1, target)
    return self.count


  # -1, 1, 2, 3, 4
  def search_pair(self, arr, first, start_idx, target) -> int:
    for i in range(start_idx, len(arr) - 1):
      for j in range(i + 1, len(arr)):
        if first + arr[i] + arr[j] < target:
          self.count += 1


def main():
  print(TripletsWithSmallerSum().triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(TripletsWithSmallerSum().triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()