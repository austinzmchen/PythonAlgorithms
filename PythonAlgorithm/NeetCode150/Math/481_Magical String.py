# Visual Example
# Step 0: [1, 2, 2]
#         ^read_ptr

# Step 1: Read s[2]=2, add 2 copies of '1'
#         [1, 2, 2, 1, 1]
#             ^read_ptr, current=1→2

# Step 2: Read s[3]=1, add 1 copy of '2'
#         [1, 2, 2, 1, 1, 2]
#               ^read_ptr, current=2→1

# Step 3: Read s[4]=1, add 1 copy of '1'
#         [1, 2, 2, 1, 1, 2, 1]
#                 ^read_ptr, current=1→2

# And so on...

class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i_t = 2 # idx for number of times to add
        num_to_add = 1 # values to add, alternating

        while len(s) < n:
            times_to_add = s[i_t]

            while times_to_add > 0:
                s.append(num_to_add)
                times_to_add -= 1
            
            num_to_add = 1 if num_to_add == 2 else 2
            i_t += 1
        
        # print(f"{s=}")

        # count the 1s
        res = 0
        for j in range(n):
            if s[j] == 1:
                res += 1
        
        return res


print(Solution().magicalString(7))