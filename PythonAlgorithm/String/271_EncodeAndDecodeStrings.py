class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for _str in strs:
          res += len(_str)
          res += ':'
          res += _str
        #
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        i = 0
        res = []
        #
        while i < len(str):
          j = i
          while j < len(str) and str[j] != ':':
            j += 1
          count = int(str[i:j])
          word = str[j+1: j+1+count]
          res.append(word)
          i = j+1+count
        #
        return res