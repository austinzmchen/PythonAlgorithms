# // check out leetcode 22. Generate Parentheses

# /*
# Problem Statement #
# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

# Example 1:

# Input: N=2
# Output: (()), ()()
# Example 2:

# Input: N=3
# Output: ((())), (()()), (())(), ()(()), ()()()

# Solution #
# This problem follows the Subsets pattern and can be mapped to Permutations. We can follow a similar BFS approach.

# Let’s take Example-2 mentioned above to generate all the combinations of balanced parentheses. Following a BFS approach, we will keep adding open parentheses ( or close parentheses ). At each step we need to keep two things in mind:

# We can’t add more than ‘N’ open parenthesis.
# To keep the parentheses balanced, we can add a close parenthesis ) only when we have already added enough open parenthesis (. For this, we can keep a count of open and close parenthesis with every combination.
# Following this guideline, let’s generate parentheses for N=3:

# Start with an empty combination: “”
# At every step, let’s take all combinations of the previous step and add ( or ) keeping the above-mentioned two rules in mind.
# For the empty combination, we can add ( since the count of open parenthesis will be less than ‘N’. We can’t add ) as we don’t have an equivalent open parenthesis, so our list of combinations will now be: “(”
# For the next iteration, let’s take all combinations of the previous set. For “(” we can add another ( to it since the count of open parenthesis will be less than ‘N’. We can also add ) as we do have an equivalent open parenthesis, so our list of combinations will be: “((”, “()”
# In the next iteration, for the first combination “((”, we can add another ( to it as the count of open parenthesis will be less than ‘N’, we can also add ) as we do have an equivalent open parenthesis. This gives us two new combinations: “(((” and “(()”. For the second combination “()”, we can add another ( to it since the count of open parenthesis will be less than ‘N’. We can’t add ) as we don’t have an equivalent open parenthesis, so our list of combinations will be: “(((”, “(()”, ()("
# Following the same approach, next we will get the following list of combinations: “((()”, “(()(”, “(())”, “()((”, “()()”
# Next we will get: “((())”, “(()()”, “(())(”, “()(()”, “()()(”
# Finally, we will have the following combinations of balanced parentheses: “((()))”, “(()())”, “(())()”, “()(())”, “()()()”
# We can’t add more parentheses to any of the combinations, so we stop here.
# Here is the visual representation of this algorithm:
#  */

def generate_valid_parentheses_1(num):
  res = []
  
  def recur(ls: list[str], num_open_left, num_close_left):
    if num_open_left == 0 and num_close_left == 0:
      res.append("".join(ls))
      
    if num_open_left > num_close_left or \
      num_open_left < 0 or \
      num_close_left < 0:
      return

    ls2 = list(ls)
    ls2.append("(")
    recur(ls2, num_open_left - 1, num_close_left)

    ls1 = list(ls)
    ls1.append(")")
    recur(ls1, num_open_left, num_close_left - 1)

  recur([], num, num)
  return res


def generate_valid_parentheses(num: int) -> list[str]:
    from collections import deque
    queue = deque([(0, 0, "")])
    
    for i in range(num * 2):
        size = len(queue)
        for j in range(size):
            open_count, close_count, value = queue.popleft()
            
            if open_count < num:
                queue.append((open_count + 1, close_count, value + "("))
            
            if close_count < open_count: # close count should not be equal or more than open c
                queue.append((open_count, close_count + 1, value + ")"))
    
    return [t[2] for t in queue]
  

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))

main()
