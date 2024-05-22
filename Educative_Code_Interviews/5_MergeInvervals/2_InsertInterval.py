def insert(intervals, newInterval):
  merged = []
  i = 0

  while i < len(intervals) and intervals[i][1] < newInterval[0]:
    merged.append(list(intervals[i]))
    i += 1
  
  curr = list(newInterval)
  for j in range(i, len(intervals)):
    inv = intervals[j]
    if inv[0] <= curr[1]:
      curr = [min(curr[0], inv[0]), max(curr[1], inv[1])]
    else:
      merged.append(curr)
      curr = list(inv)

  merged.append(curr)
  return merged


def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()