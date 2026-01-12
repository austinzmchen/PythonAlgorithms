class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        res = []

        for n in nums:
            size = len(perms)
            for p in range(size):
                for i in range(len(perms[p]) + 1):
                    new_perm = list(perms[p])
                    new_perm.insert(i, n)
                    perms.append(new_perm)

                    if len(new_perm) == len(nums):
                        res.append(new_perm)
        return res