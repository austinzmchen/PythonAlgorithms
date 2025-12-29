
def search_next_letter(letters, key):
  l, r = 0, len(letters) - 1
  
  while l <= r:
    mid = r + (l - r) // 2
    
    if key < letters[mid]:
      r = mid - 1
    else:
      l = mid + 1

  if l >= len(letters):
    return letters[0]
  return letters[l]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))

main()