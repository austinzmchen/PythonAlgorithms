class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        _dict = {}
        for i, c in enumerate(s):
            _dict[c] = i # take the higher index

        inv = [0, 0]
        res = []

        for i, c in enumerate(s):
            # for each char, find the max index
            max_i = max(i, _dict[c])
            # for each char before the interval, push the max end
            inv[1] = max(inv[1], max_i)

            # if when reaching to the end of the interval
            if i == inv[1]:
                res.append(inv[1] - inv[0] + 1)
                inv = [i + 1, 0]
        
        return res