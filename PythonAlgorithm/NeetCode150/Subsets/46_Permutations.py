class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        res = []

        for n in nums:
            size = len(perms)
            for p in range(size):
                for i in range(len(perms[p]) + 1):
                    ls = list(perms[p])
                    ls.insert(i, n)
                    perms.append(ls)

                    if len(ls) == len(nums):
                        res.append(ls)
        return res