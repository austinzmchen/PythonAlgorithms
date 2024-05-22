def find_max_sum_subsequence(nums):
  def recur(idx):
    if idx >= len(nums):
      return 0
    return max(nums[idx] + recur(idx + 2), recur(idx + 1))
  #
  return recur(0)


print(find_max_sum_subsequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))