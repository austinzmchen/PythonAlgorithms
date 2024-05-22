from collections import defaultdict, deque


def find_order(words):
  sortedOrder = []
  adj_dict = defaultdict(list)
  in_degrees = defaultdict(int)

  for i in range(1, len(words)):
    prev_word = words[i - 1]
    curr_word = words[i]
    for j in range(min(len(prev_word), len(curr_word))):
      if prev_word[j] != curr_word[j]:
        adj_dict[prev_word[j]].append(curr_word[j])
        
        in_degrees[prev_word[j]] = in_degrees[prev_word[j]]
        in_degrees[curr_word[j]] += 1
        break

  queue = deque()
  for key, value in in_degrees.items():
    if value == 0:
      queue.append(key)

  while len(queue) > 0:
    size = len(queue)
    for i in range(size):
      n = queue.popleft()
      sortedOrder.append(n)

      for adj in adj_dict[n]:
        in_degrees[adj] -= 1
        if in_degrees[adj] == 0:
          queue.append(adj)

  return "".join(sortedOrder)


def main():
  print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
  print("Character order: " + find_order(["cab", "aaa", "aab"]))
  print("Character order: " +
        find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))
  
  print("Character order: " + find_order(["zy","zx"]))

main()
