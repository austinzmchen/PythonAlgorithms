def generate_valid_parentheses(num):
  result = []
  recur(result, [], num, num)
  return result


def recur(result, ls, num_open, num_close):
  if num_open == 0 and num_close == 0:
    result.append("".join(ls))

  if num_open > num_close or num_open < 0 or num_close < 0:
    return

  ls2 = list(ls)
  ls2.append("(")
  recur(result, ls2, num_open - 1, num_close)

  ls1 = list(ls)
  ls1.append(")")
  recur(result, ls1, num_open, num_close - 1)


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()
