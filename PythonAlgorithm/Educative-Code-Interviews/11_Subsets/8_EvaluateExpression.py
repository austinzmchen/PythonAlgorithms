
def diff_ways_to_evaluate_expression(input):
  res = []

  # if input is just a number
  if all(sign not in input 
         for sign in ["+", "-", "*"]):
    res.append(int(input))
    return res

  for i, char in enumerate(input):
    if not char.isdigit():
      lefts = diff_ways_to_evaluate_expression(input[:i])
      rights = diff_ways_to_evaluate_expression(input[i + 1:])

      for part1 in lefts:
          for part2 in rights:
            if char == '+':
              res.append(part1 + part2)
            elif char == '-':
              res.append(part1 - part2)
            elif char == '*':
              res.append(part1 * part2)

  return res


cache: dict[str, list[int]] = {}

def diff_ways_to_evaluate_expression_v2(input_str: str) -> list[int]:
    if input_str not in cache:
        # Base case
        if '+' not in input_str and '-' not in input_str and '*' not in input_str:
            return [int(input_str)]
        
        res = []
        for i, chr in enumerate(input_str):
            if not chr.isdigit():
                left_parts = diff_ways_to_evaluate_expression_v2(input_str[:i])
                right_parts = diff_ways_to_evaluate_expression_v2(input_str[i + 1:])
                
                for part1 in left_parts:
                    for part2 in right_parts:
                        if chr == '+':
                            res.append(part1 + part2)
                        elif chr == '-':
                            res.append(part1 - part2)
                        elif chr == '*':
                            res.append(part1 * part2)
        
        cache[input_str] = res
    
    return cache[input_str]
  
  
def main():
  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("1+2*3")))

  print("Expression evaluations: " +
        str(diff_ways_to_evaluate_expression("2*3-4-5")))

main()
