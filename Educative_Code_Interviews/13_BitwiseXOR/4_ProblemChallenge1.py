def flip_and_invert_image(matrix):
  for row in matrix:
    row.reverse()
    for j in range(len(row)):
      row[j] = 1 ^ row[j]
  return matrix


def main():
  print(flip_and_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
  print(flip_and_invert_image(
      [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
