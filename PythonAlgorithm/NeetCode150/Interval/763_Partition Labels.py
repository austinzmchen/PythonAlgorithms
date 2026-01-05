class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        _dict = {}
        for i, c in enumerate(s):
            _dict[c] = i # take the higher index

        inv = (0, 0)
        res = []

        for i, c in enumerate(s):
            max_i = max(i, _dict[c])
            inv = (inv[0], max(inv[1], max_i))

            if i == inv[1]:
                res.append(inv[1] - inv[0] + 1)
                inv = (i + 1, 0)
        
        return res