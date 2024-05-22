from heapq import heapify, heappop, heappush


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
  min_heap = []
  for i in range(len(capital)):
    heappush(min_heap, (capital[i], i))

  max_heap_profits = []
  money = initialCapital

  while numberOfProjects > 0:
    while len(min_heap) > 0 and min_heap[0][0] <= money:
      cap, idx = heappop(min_heap)
      heappush(max_heap_profits, -profits[idx])

    money += -max_heap_profits[0]
    numberOfProjects -= 1

  return money


def main():

  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
  print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
