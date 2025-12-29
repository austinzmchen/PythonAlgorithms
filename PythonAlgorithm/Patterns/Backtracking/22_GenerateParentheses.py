class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def recur(path, open_num, close_num):
            if open_num == 0 and close_num == 0:
                results.append(path)
                return
            if open_num > 0:
                recur(path + "(", open_num-1, close_num)
            if open_num < close_num:
                recur(path + ")", open_num, close_num-1)
        #
        recur("", n, n)
        return results