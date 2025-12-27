# LeetCode 252: Meeting Rooms
# Difficulty: Easy
# Problem Description
# Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine if a person could attend all meetings.
# In other words, check if there are any overlapping meetings.

# Examples

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Explanation: [0,30] overlaps with [5,10] and [15,20]

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true
# Explanation: No overlapping meetings

# Example 3:
# Input: intervals = [[1,5],[8,9]]
# Output: true

class Solution_252:
    def canAttendMeetings(intervals: List) -> bool:
        intervals.sort()
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            inv = intervals[i]
            
            if inv[0] < end: # equal not okay?
                return False
            
        return True