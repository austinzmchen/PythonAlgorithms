class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        _set = set()

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == ".":
                    continue

                if f"{cell},{r=}" in _set or \
                    f"{cell},{c=}" in _set or \
                    f"{cell},{r//3},{c//3}" in _set:
                    
                    return False

                _set.add(f"{cell},{r=}")
                _set.add(f"{cell},{c=}")
                _set.add(f"{cell},{r//3},{c//3}")

        return True