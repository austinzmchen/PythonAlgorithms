def backspace_compare(str1, str2):
  i1 = len(str1) - 1
  i2 = len(str2) - 1

  while True:
    i1 = get_next_valid_char_index(str1, i1)
    i2 = get_next_valid_char_index(str2, i2)

    if i1 < 0 or i2 < 0:
      return False
    elif str1[i1] != str2[i2]:
      return False
    
    if i1 == 0 and i2 == 0:
      return True
    
    i1 -= 1
    i2 -= 1



def get_next_valid_char_index(str, index):
  count = 0
  while index >= 0:
    if str[index] == '#':
      count += 1
      index -= 1
    elif count > 0:
      count -= 1
      index -= 1
    else:
      break
  
  return index


def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
