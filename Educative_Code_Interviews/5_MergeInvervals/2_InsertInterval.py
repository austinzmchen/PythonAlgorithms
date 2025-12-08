# /*
# Problem Statement #
# Given a list of non-overlapping intervals sorted by their start time, 
# insert a given interval at the correct position and merge all necessary intervals 
# to produce a list that has only mutually exclusive intervals.

# Example 1:
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

# Example 2:
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

# Example 3:
# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
#
# */

def insert(intervals, new_interval):
  merged = []
  i = 0

  for _, inv in enumerate(intervals):
    if inv[1] < new_interval[0]:
      merged.append(inv)
      i += 1
    else: break
  
  start, end = new_interval[0], new_interval[1]

  for _, inv in enumerate(intervals[i:], start=i):
    if inv[0] <= end:
      start, end = min(start, inv[0]), max(end, inv[1])
    else:
      merged.append([start, end])
      start, end = inv[0], inv[1] #

  merged.append([start, end])
  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()