from typing import DefaultDict


def find_string_anagrams(str, pattern):
    _dict = DefaultDict(int)
    for p in pattern:
        _dict[p] += 1
    
    _count = len(_dict)
    _list = []

    for win_end in range(len(str)):
        c = str[win_end]
        if c in _dict:
            _dict[c] -= 1
            if _dict[c] == 0:
                _count -= 1
        
        c_start = win_end - len(pattern)
        if c_start >= 0:
            if str[c_start] in _dict:
                if _dict[str[c_start]] == 0:
                    _count += 1
                _dict[str[c_start]] += 1

        if _count == 0:
            _list.append(c_start + 1)

    return _list

def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()