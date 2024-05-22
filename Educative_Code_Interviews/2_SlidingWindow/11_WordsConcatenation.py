from typing import DefaultDict


def find_word_concatenation(str, words):
  WL = len(words[0])

  _ddict = DefaultDict(int)
  for word in words:
    _ddict[word] += 1

  match = 0
  winS = 0
  result_indices = []

  for winE in range(0, len(str) - WL + 1, WL):
    w = str[winE: winE + WL]
    if w in _ddict:
      _ddict[w] -= 1
      if _ddict[w] == 0:
        match += 1
    
    if winE - winS + 1 > WL * len(words):
      lw = str[winS: winS + WL]
      if lw in _ddict:
        if _ddict[lw] == 0:
          match -= 1
        _ddict[lw] += 1
        
      winS += WL

    if match == len(_ddict):
      result_indices.append(winS)

  return result_indices


def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()