# """
# Check if the original sequence can be UNIQUELY reconstructed from the subsequences.

# Args:
#     original_seq: The original sequence to reconstruct
#     sequences: List of subsequences

# Returns:
#     True if original_seq is the only sequence that can be reconstructed, False otherwise
# """

from collections import deque

def can_construct(original_seq, sequences):
  adj_dict: dict[str, list] = {}
  in_degrees: dict[str, int] = {}
  
  for seq in sequences:
    for i in range(len(seq) - 1):
      from_node = seq[i]
      to_node = seq[i + 1]
      
      adj_dict.setdefault(from_node, []).append(to_node)
      
      in_degrees.setdefault(from_node, 0)
      in_degrees[to_node] = in_degrees.setdefault(to_node, 0) + 1
      
  queue = deque()
  for k, v in in_degrees.items():
    if v == 0:
      queue.append(k)

  i = 0
  while queue:
    # queue size should be 1 at any time so to uniquely reconstruct
    if len(queue) > 1 or queue[0] != original_seq[i]:
      return False
    
    n = queue.popleft()
    i += 1
    
    for adj in adj_dict.get(n, []):
      if adj in in_degrees:
        in_degrees[adj] -= 1
        if in_degrees[adj] == 0:
          queue.append(adj)

  return True


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))

main()