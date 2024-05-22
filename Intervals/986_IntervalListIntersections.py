from typing import List


class Solution986:
  def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i, j = 0, 0
    res = []
    while i < len(firstList) and j < len(secondList):
      if (secondList[j][0] <= firstList[i][0] <= secondList[j][1]) or (firstList[i][0] <= secondList[j][0] <= firstList[i][1]):
        s = max(firstList[i][0], secondList[j][0])
        e = min(firstList[i][1], secondList[j][1])
        res.append([s, e])

      if firstList[i][1] < secondList[j][1]:
        i += 1
      else:
        j += 1
    return res
