def find_subarrays(arr, target):
  result = []
  for i in range(len(arr)):
    if arr[i] >= target: continue
    list = [arr[i]]
    result.append(list.copy())
    product = arr[i]

    for j in range(i + 1, len(arr)): 
      product *= arr[j]
      if product < target:
        list.append(arr[j])
        result.append(list.copy())

  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()