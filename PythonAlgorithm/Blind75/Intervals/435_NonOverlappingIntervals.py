class Solution:
    
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda ls: ls[0])
        start, end = intervals[0]
        res = 0

        for i in range(1, len(intervals)):
            inv = intervals[i]

            if inv[0] < end:
                # overlaps
                res += 1
                
                # this may not correspond to any interval,
                # basically we want the smaller end inv
                # e.g. [[1,100],[1,11],[2,12],[11,22]]
                end = min(end, inv[1])
            else:
                start, end = inv

        return res        
