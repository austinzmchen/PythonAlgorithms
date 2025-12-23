
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        _dict = {}
        for i, v in enumerate(nums):
            if target - v in _dict:
                return [_dict[target - v], i]
            _dict[v] = i
        raise Exception("not found")