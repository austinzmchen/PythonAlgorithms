def make_squares(arr):
  squares = []
  left, right = 0, len(arr) - 1
  while left <= right:
    lv, rv = arr[left], arr[right]
    if lv ** 2 >= rv ** 2:
      squares.insert(0, lv ** 2)
      left += 1
    else:
      squares.insert(0, rv ** 2)
      right -= 1

  return squares

def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()