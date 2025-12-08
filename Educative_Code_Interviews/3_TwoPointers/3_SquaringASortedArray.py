# /*
# Problem Statement #
# Given a sorted array, create a new array containing squares of all the numbers of 
# the input array in the sorted order.

# Example 1:
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

# Example 2:
# Input: [-3, -1, 0, 1, 2]
# Output: [0, 1, 1, 4, 9]
#  */

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