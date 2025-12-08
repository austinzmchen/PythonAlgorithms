# find smallest substring that contains the pattern

def find_substring(str, pattern):
    import sys
    res_idx, max_len = 0, sys.maxsize
    _dict = {}

    for p in pattern:
        _dict[p] = _dict.setdefault(p, 0) + 1
    count = len(_dict)

    win_start = 0
    for win_end, v in enumerate(str):
        if v in _dict:
            _dict[v] -= 1
            if _dict[v] == 0:
                count -= 1
        
        while count == 0:
            char_s = str[win_start]
            if char_s in _dict:
                if _dict[char_s] == 0:
                    count += 1
                _dict[char_s] += 1

            # update min substring
            if win_end - win_start + 1 < max_len:
                max_len = win_end - win_start + 1
                res_idx = win_start

            win_start += 1

    return (str[res_idx : res_idx + max_len]
            if max_len != sys.maxsize
            else "")


def main():
  print('"aabdec", "abc"' + ":" + find_substring("aabdec", "abc"))
  print('"abdbca", "abc"' + ":" + find_substring("abdbca", "abc"))
  print('"adcad",  "abc"' + ":" + find_substring("adcad", "abc"))

main()