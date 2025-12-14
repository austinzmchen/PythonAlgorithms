class Solution:
    def calculate(self, s: str) -> int:
        nums, ops = [], []
        i = 0
        while i < len(s):
            if s[i] == '+' or \
                s[i] == '-' or \
                s[i] == '*' or \
                s[i] == '/':
                ops.append(s[i])
                i += 1
            elif s[i] == ' ':
                i += 1
                continue
            else:
                d_str = ''
                while i < len(s) and s[i].isdigit():
                    d_str += s[i]
                    i += 1
                nums.append(int(d_str))
                #
                if len(ops) > 0 and (ops[-1] == '*' or ops[-1] == '/'):
                    b, a = nums.pop(), nums.pop()
                    op = ops.pop()
                    if op == '*':
                        nums.append(a * b)
                    elif op == '/':
                        nums.append(a // b)
        #
        nums, ops = nums[::-1], ops[::-1]
        while len(nums) > 1:
            a, b = nums.pop(), nums.pop()
            op = ops.pop()
            if op == '+':
                num = a + b
            elif op == '-':
                num = a - b
            nums.append(num)
        #
        return nums[0]
            