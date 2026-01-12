class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            size = len(res)
            for i in range(size):
                new_ls = list(res[i])
                new_ls.append(n)
                res.append(new_ls)
        
        return res