class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        res = []
        digit2char = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def recur(i, path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            for c in digit2char[digits[i]]:
                recur(i + 1, path + c)

        recur(0, "")
        return res