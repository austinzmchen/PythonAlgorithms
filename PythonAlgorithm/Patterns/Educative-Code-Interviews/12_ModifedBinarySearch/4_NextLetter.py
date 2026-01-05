
def search_next_letter(letters, key):
  l, r = 0, len(letters) - 1
  
  while l <= r:
    mid = r + (l - r) // 2
    
    if key < letters[mid]:
      r = mid - 1
    else:
      l = mid + 1

  if l < len(letters):
    return letters[0]
  return letters[l]


def search_next_letter(letters, key):
  l, r = 0, len(letters) - 1
  
  while l <= r:
    mid = (l + r) // 2
    
    if letters[mid] == key:
      # return next
      if mid + 1 < len(letters):
        return letters[mid + 1]
      else:
        return letters[0]
    
    if key < letters[mid]:
      r = mid - 1
    
    else:
      l = mid + 1
  
  # return the immediate 
  if l < len(letters):
    return letters[l + 1]
  else:
    return letters[0]
      
    
  
def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'h'))

main()