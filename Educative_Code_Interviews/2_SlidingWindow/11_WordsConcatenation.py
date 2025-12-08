

def find_word_concatenation_1(str, words):
  WL = len(words[0])

  _dict = {}
  for word in words:
    _dict[word] = _dict.setdefault(word, 0) + 1

  match = 0
  win_s = 0
  res = []

  for win_e in range(0, len(str) - WL + 1, WL):
    w = str[win_e: win_e + WL]
    if w in _dict:
      _dict[w] -= 1
      if _dict[w] == 0:
        match += 1
    
    if win_e - win_s + 1 > WL * len(words):
      lw = str[win_s: win_s + WL]
      if lw in _dict:
        if _dict[lw] == 0:
          match -= 1
        _dict[lw] += 1
        
      win_s += WL

    if match == len(_dict):
      res.append(win_s)

  return res

def find_word_concatenation(str, words):
  WL = len(words[0]) # assume words length are the same

  _dict = {}
  for word in words:
    _dict[word] = _dict.setdefault(word, 0) + 1
  match = 0
  res = []

  for win_e in range(WL, len(str) + 1, WL):
    # update _dict and `match`
    w = str[win_e - WL: win_e]
    if w in _dict:
      _dict[w] -= 1
      if _dict[w] == 0:
        match += 1
      
    win_s = win_e - WL * len(words)
    if win_s - WL >= 0:
      lw = str[win_s - WL: win_s]
      if lw in _dict:
        if _dict[lw] == 0:
          match -= 1
        _dict[lw] += 1
        
      win_s += WL
    
    if match == len(_dict):
      res.append(win_e - WL * len(words))
  return res


def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()