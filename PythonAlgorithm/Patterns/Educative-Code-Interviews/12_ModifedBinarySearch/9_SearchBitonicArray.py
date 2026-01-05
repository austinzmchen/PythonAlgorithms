
def search_bitonic_array(arr, key):
  l, r = 0, len(arr) - 1
  while l < r:
    mid = l + (r - l) // 2

    if arr[mid] == key:
      return mid
    
    if arr[mid] < arr[mid + 1]:
      if key <= arr[mid + 1]:
        return order_argnostic_binary_search(arr, key, l, mid + 1)
      else:
        l = mid + 1
        
    else:
      if key <= arr[mid]:
        return order_argnostic_binary_search(arr, key, mid, r)
      else:
        r = mid
        
  return -1


# copied from the first question
def order_argnostic_binary_search(arr, key, start_idx, end_idx):
  l, r = start_idx, end_idx
  
  while l <= r:
    mid = r + (l - r) // 2
    if arr[mid] == key:
      return mid

    if arr[l] < arr[r]:  # ascending
      if key < arr[mid]:
        r = mid - 1
      else:
        l = mid + 1
    else:
      if key < arr[mid]:
        l = mid + 1
      else:
        r = mid - 1
  return -1


# 1. find the peak index
# 2. search asc
# 3, search desc

def search_bitonic_array(arr, key):
  l, r = 0, len(arr) - 1
  
  # find the peak index first
  while l < r:
    mid = (l + r) // 2
    if arr[mid] == key:
      return mid
    
    if arr[mid] < arr[mid + 1]:
      l = mid + 1
    
    else:
      r = mid
  
  peak_i = l
  
  def find_asc(key, start, end):
    while start <= end:
      m = (start + end) // 2
      if arr[m] == key:
        return m
      
      if key < arr[m]:
        end = m - 1
      else:
        start = m + 1
    return None
  
  def find_desc(key, start, end):
    while start <= end:
      m = (start + end) // 2
      if arr[m] == key:
        return m
      
      if key < arr[m]:
        start = m + 1
      else:
        end = m - 1
    return None
  
  if (i := find_asc(key, 0, peak_i)) is not None:
    return i
  
  if (i := find_desc(key, peak_i, len(arr) - 1)) is not None:
    return i
  
  return -1
  
  
def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))

main()