import sys
from typing import DefaultDict

def find_substring(str, pattern):
    c_start, max_len = 0, sys.maxsize
    _dict = DefaultDict(int)

    for p in pattern:
        _dict[p] += 1

    _count = len(_dict)

    win_start = 0
    for win_end in range(len(str)):
        c = str[win_end]
        if c in _dict:
            _dict[c] -= 1
            if _dict[c] == 0:
                _count -= 1
        
        while _count == 0:
            if str[win_start] in _dict:
                if _dict[str[win_start]] == 0:
                    _count += 1
                _dict[str[win_start]] += 1

            if win_end - win_start + 1 < max_len:
                max_len = win_end - win_start + 1
                c_start = win_start

            win_start += 1

    return str[c_start : c_start + max_len] if max_len != sys.maxsize else ""


def main():
  print(find_substring("aabdec", "abc"))
  print(find_substring("abdbca", "abc"))
  print(find_substring("adcad", "abc"))

main()