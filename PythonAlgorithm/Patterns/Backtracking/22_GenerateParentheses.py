class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def recur(path, open_num, close_num):
            if open_num == 0 and close_num == 0:
                res.append(path)
                return
            
            if open_num > 0:
                recur(path + "(", open_num - 1, close_num)
            if open_num < close_num:
                recur(path + ")", open_num, close_num - 1)

        recur("", n, n)
        return res
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recur(open, close, path):
            if open == n and close == n:
                res.append(path)
                return
            if open > n or close > n:
                return
            if close > open:
                return

            recur(open + 1, close, path + "(")
            recur(open, close + 1, path + ")")
        
        recur(0, 0, "")
        return res
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recur(open, close, path):
            if open == n and close == n:
                res.append(path)
                return
            if open > n or close > n:
                return
            
            recur(open + 1, close, path + "(")
            if open > close:
                recur(open, close + 1, path + ")")
        
        recur(0, 0, "")
        return res