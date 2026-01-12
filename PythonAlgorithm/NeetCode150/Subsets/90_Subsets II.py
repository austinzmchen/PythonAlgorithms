class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        for n in nums:
            size = len(res)
            for i in range(size):
                new_ls = list(res[i])
                new_ls.append(n)
                res.append(new_ls)
        
        _set = set()
        for ls in res:
            _set.add(tuple(ls))
        
        return [list(t) for t in _set]