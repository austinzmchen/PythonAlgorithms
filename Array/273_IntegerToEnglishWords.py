class Solution:
    def numberToWords(self, num: int) -> str:
        _dict = {
            0 : '',
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
            10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
            100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'
        }
        #
        ls = []
        n = num
        while n > 0:
            v = n % 1000
            ls.append(v)
            n //= 1000
        #
        results = []
        for i, nv in enumerate(ls[::-1]):
            j = 0
            #
            if 10 <= nv % 100 < 20:
                results.insert(0, _dict[nv])
                n //= 100
                j == 2
            #
            while nv > 0:
                d = nv % 10
                k = d * 10 ** j
                results.insert(0, _dict[k])
                j += 1
                nv //= 10
            #
            if i > 0:
                thousand = 1000 ** i
                results.insert(0, _dict[thousand])
        #
        return ' '.join(results)
      
    
    def numberToWords(self, num: int) -> str:
        _dict = {
            0 : '',
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
            10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
            100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'
        }
        #
        ls = []
        n = num
        while n > 0:
            v = n % 1000
            ls.insert(0, v)
            n //= 1000
        #
        results = []
        for i in range(len(ls)-1, -1, -1):
            nv = ls[i]
            j = 0
            #
            idx = len(ls) - 1 - i
            if idx > 0:
                if nv % 1000 != 0:
                    thousand = 1000 ** idx
                    results.insert(0, _dict[thousand])
            #
            if 10 <= nv % 100 < 20:
                results.insert(0, _dict[nv % 100])
                nv //= 100
                j == 2
            else:
                results.insert(0, _dict[nv % 10])
                nv //= 10
                results.insert(0, _dict[nv % 10 * 10])
                nv //= 10
            #
            if nv > 0:
                results.insert(0, _dict[100])
                results.insert(0, _dict[nv % 10])
                nv //= 10
        #
        results = list(filter(lambda x: x, results))
        return ' '.join(results)
      
      
print(Solution().numberToWords(12345))
print(Solution().numberToWords(110))
print(Solution().numberToWords(1000000))