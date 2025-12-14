class Solution_252:
    def canAttendMeetings(intervals: List) -> bool:
        intervals.sort()
        curr = intervals[0]

        for i in range(1, len(intervals)):
            inv = intervals[i]
            if curr[1] >= inv[0]:
                return False
            
        return True