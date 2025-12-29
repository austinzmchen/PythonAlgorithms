# Problem Statement
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

# Flip horizontally: Reverse each row
# Invert: Replace 0s with 1s and 1s with 0s

# Example:
# Input: [[1,1,0],
#         [1,0,1],
#         [0,0,0]]

# After flip: [[0,1,1],
#              [1,0,1],
#              [0,0,0]]

# After invert: [[1,0,0],
#                [0,1,0],
#                [1,1,1]]

# Output: [[1,0,0],
#          [0,1,0],
#          [1,1,1]]

def flip_and_invert_image(matrix):
  for row in matrix:
    row.reverse()
    for j, v in enumerate(row):
      row[j] = 1 ^ v
  return matrix


def main():
  print(flip_and_invert_image([[1, 0, 1], 
                               [1, 1, 1], 
                               [0, 1, 1]]))
  print(flip_and_invert_image(
      [[1, 1, 0, 0], 
       [1, 0, 0, 1], 
       [0, 1, 1, 1], 
       [1, 0, 1, 0]]))

main()
