class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(w: str) -> str:
            return w[::-1]
        #
        ls = [reverse(w) for w in reverse(s).split()]
        return ' '.join(ls)
            