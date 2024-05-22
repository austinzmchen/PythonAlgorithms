class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr = intervals[0]

        res = 0
        for i in range(1, len(intervals)):
            inv = intervals[i]
            if curr[1] <= inv[0]:
                curr = list(inv)
            else:
                curr[1] = min(curr[1], inv[1])
                res += 1
        
        return res