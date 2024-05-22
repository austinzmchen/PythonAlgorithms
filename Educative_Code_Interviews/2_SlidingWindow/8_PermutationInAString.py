from typing import DefaultDict


def find_permutation(str, pattern):
    _dict = DefaultDict(int)
    for c in pattern:
        _dict[c] += 1
    
    _count = len(_dict)

    for winE in range(len(str)):
        c = str[winE]
        if c in _dict:
            _dict[c] -= 1
            if _dict[c] == 0: _count -= 1

        if winE >= len(pattern):
            c_start = winE - len(pattern)

            if str[c_start] in _dict:
                if _dict[str[c_start]] == 0:
                    _count += 1
                _dict[str[c_start]] += 1
        
        if _count == 0:
            return True
    
    return False


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()