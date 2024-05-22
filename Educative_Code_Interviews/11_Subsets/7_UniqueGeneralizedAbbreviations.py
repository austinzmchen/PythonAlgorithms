def generate_generalized_abbreviation(word):
  result = []
  result.append(("", 0))

  for c in word:
    size = len(result)
    for i in range(size):
      holder = result[0]
      del result[0]

      # add new char
      result.append((f"{holder[0]}{c}", 0))
      # add abbrev count
      if holder[1] == 0:
        result.append((f"{holder[0]}1", 1))
      else:
        str = holder[0][0:-1]
        count = holder[1] + 1
        result.append((f"{str}{count}", count))

  return [v[0] for v in result]


def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()
