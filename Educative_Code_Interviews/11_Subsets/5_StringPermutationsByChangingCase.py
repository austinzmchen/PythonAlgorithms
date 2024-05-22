def find_letter_case_string_permutations(str):
  perms = []
  perms.append("")

  for c in str:
    size = len(perms)
    for i in range(size):
      p = perms[0]
      del perms[0]

      if c.isalpha():
        perms.append(f"{p}{c.lower()}")
        perms.append(f"{p}{c.upper()}")
      else:
        perms.append(f"{p}{c}")

  return ["".join(p) for p in perms]


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
