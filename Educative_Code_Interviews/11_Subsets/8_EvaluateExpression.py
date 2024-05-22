def diff_ways_to_evaluate_expression(input):
  result = []

  if all(sign not in input for sign in ["+", "-", "*"]):
    result.append(int(input))
    return result

  for i, char in enumerate(input):
    if not char.isdigit():
      lefts = diff_ways_to_evaluate_expression(input[:i])
      rights = diff_ways_to_evaluate_expression(input[i + 1:])

      for part1 in lefts:
          for part2 in rights:
            if char == '+':
              result.append(part1 + part2)
            elif char == '-':
              result.append(part1 - part2)
            elif char == '*':
              result.append(part1 * part2)

  return result


def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
