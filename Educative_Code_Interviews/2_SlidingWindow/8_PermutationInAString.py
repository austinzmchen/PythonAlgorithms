
def find_permutation(str, pattern) -> bool:
    _dict = {}
    for v in pattern:
        _dict[v] = _dict.setdefault(v, 0) + 1
    count = len(_dict) # count of distinct chars in pattern

    for win_e, v in enumerate(str):
        # update count
        if v in _dict:
            _dict[v] -= 1
            if _dict[v] == 0:
                count -= 1
        
        if count == 0:
            return True
        
        win_s = win_e - len(pattern) + 1
        if win_s >= 0:
            char_s = str[win_s]
            # update count as win_s idx is updated
            if char_s in _dict:
                if _dict[char_s] == 0: # 0 not deleted
                    count += 1
                _dict[char_s] += 1

    return False


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()