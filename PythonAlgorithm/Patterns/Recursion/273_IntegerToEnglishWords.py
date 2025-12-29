class Solution273:
  
    def __init__(self) -> None:
        self.less20 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        self.tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        self.thousands = ["Thousand", "Million", "Billion"]
    
    def numberToWords2(self, num: int) -> str:
        if num == 0: 
            return "Zero"
        #
        res = []
        i = 0
        while num > 0:
            n = num % 1000
            if n > 0:
                if i > 0:
                    res.insert(0, self.thousands[i-1])
                self.dfs(res, n)
            #
            num //= 1000
            i += 1
        #
        return " ".join(res)
    
    def dfs(self, list, num):
        if 0 < num < 20:
          list.insert(0, self.less20[num-1])
        elif num < 100:
          self.dfs(list, num%10)
          list.insert(0, self.tens[num//10-2])
        else:
          self.dfs(list, num%100)
          list.insert(0, "Hundred")
          list.insert(0, self.less20[num//100-1])
          
      
    # iterative
    def numberToWords(self, num: int) -> str:
        if num == 0: 
            return "Zero"
        #
        less20 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        thousands = ["Thousand", "Million", "Billion"]
        #
        res = []
        i = 0
        while num > 0:
            n = num % 1000
            if n > 0:
                if i > 0:
                    res.insert(0, thousands[i - 1])
                #
                if 0 < n % 100 < 20:
                    res.insert(0, less20[n % 100 - 1])
                if n % 100 >= 20:
                    if n % 100 % 10:
                        res.insert(0, less20[n % 100 % 10 - 1])
                    if n % 100 // 10 > 0:
                        res.insert(0, tens[n % 100 // 10 - 2])
                if n // 100 > 0:
                    res.insert(0, "Hundred")
                    res.insert(0, less20[n // 100 - 1])
            #
            num //= 1000
            i += 1
        #
        return " ".join(res)
      
      
# print(Solution273().numberToWords2(123))
print(Solution273().numberToWords2(12345))