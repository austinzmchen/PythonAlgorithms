# /*
# Problem Statement #
# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Example 1:
# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

# Example 2:
# Appointments: [[6,7], [2,4], [8,12]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.

# Example 3:
# Appointments: [[4,5], [2,3], [3,6]]
# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
#
#  */

 
def can_attend_all_appointments(intervals):
  if len(intervals) <= 1: 
    return True
  
  intervals.sort(key=lambda x: x[0])
  
  start, end = intervals[0][0], intervals[0][1]
  for _, inv in enumerate(intervals[1:]):
    if inv[0] <= end:
      return False
    else: 
      start, end = inv[0], inv[1]

  return True


def main():
  print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


main()