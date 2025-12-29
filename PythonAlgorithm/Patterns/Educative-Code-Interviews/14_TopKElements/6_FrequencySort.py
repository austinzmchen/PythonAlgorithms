from heapq import heappop, heappush

def sort_character_by_frequency(str):
  freq_dict = {}
  for c in str:
    freq_dict[c] = freq_dict.setdefault(c, 0) + 1

  max_heap = []
  for c, freq in freq_dict.items():
    heappush(max_heap, (-freq, c))
    
  res = []
  while max_heap:
    freq, c = heappop(max_heap)
    res.append(c * -freq)

  return "".join(res)


def main():
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))

main()