
def find_string_anagrams(str, pattern):
    _dict = {}
    for p in pattern:
        _dict[p] = _dict.setdefault(p, 0) + 1
    count = len(_dict)
    res = []

    for win_e, v in enumerate(str):
        if v in _dict:
            _dict[v] -= 1
            if _dict[v] == 0:
                count -= 1
        
        win_s = win_e - len(pattern) + 1
        if count == 0:
            res.append(win_s)
            
        if win_s >= 0:
            char_s = str[win_s]
            if char_s in _dict:
                if _dict[char_s] == 0:
                    count += 1
                _dict[char_s] += 1
    return res


def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()