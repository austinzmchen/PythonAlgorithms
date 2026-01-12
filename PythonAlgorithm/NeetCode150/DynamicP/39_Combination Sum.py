class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def recur(i, path):
            if i >= len(candidates):
                return
            if sum(path) > target:
                return

            if sum(path) == target:
                res.append(list(path))
                return
            
            recur(i, path + [candidates[i]])
            recur(i + 1, path) 
        
        recur(0, [])
        return res