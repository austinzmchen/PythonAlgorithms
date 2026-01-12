# LeetCode 253: Meeting Rooms II
# Difficulty: Medium
# Problem Description
# Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i], 
#   return the minimum number of conference rooms required.
# In other words, find the minimum number of meetings that overlap at any point in time.

# Examples

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2
# Explanation: 
# - At time 5, meetings [0,30] and [5,10] overlap → need 2 rooms
# - At time 15, meetings [0,30] and [15,20] overlap → need 2 rooms

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1
# Explanation: No meetings overlap, so only 1 room is needed

# Example 3:
# Input: intervals = [[1,5],[2,8],[6,10]]
# Output: 2
# Explanation:
# - At time 2, meetings [1,5] and [2,8] overlap → need 2 rooms
# - At time 6, meeting [2,8] hasn't ended when [6,10] starts → need 2 rooms

# Example 4:
# Input: intervals = [[1,3],[3,6],[6,8]]
# Output: 1
# Explanation: Meetings happen back-to-back with no overlap
  
  
class Solution:  
    def minMeetingRooms(intervals: list) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        intervals.sort(key=lambda ls: ls[0])
        
        from heapq import heappush, heappop
        min_heap = []
        res = 0

        for i in range(1, len(intervals)):
            inv = intervals[i]

            # compare the next meeting's start with the end of a current meeting that finishes earliest
            while min_heap and min_heap[0][0] <= inv[0]:
                # if last course ends before(or equal) current course starts
                heappop(min_heap)

            heappush(min_heap, (inv[1], i))
            res = max(res, len(min_heap))

        return res