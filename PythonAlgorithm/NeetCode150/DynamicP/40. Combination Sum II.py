
class Solution:
    # TLE
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()

        def recur(i, path):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.add(tuple(path))
                return
            
            if i >= len(candidates):
                return
            
            recur(i + 1, path + [candidates[i]])
            recur(i + 1, path) 
        
        recur(0, [])
        return [list(t) for t in res]
    

print(Solution().combinationSum2(candidates=[2,5,2,1,2], target=5))