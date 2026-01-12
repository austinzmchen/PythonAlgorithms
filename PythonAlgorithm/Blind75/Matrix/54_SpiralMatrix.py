
# this is like 2 pointers, 1 at the left 1 at right
def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    
    res = []
    top, bottom = 0, len(matrix) - 1
    l, r = 0, len(matrix[0]) - 1
    
    while top <= bottom and l <= r:
        # Move right along the top row
        for c in range(l, r + 1):
            res.append(matrix[top][c])
        top += 1
        
        # Move down along the right column
        for r in range(top, bottom + 1):
            res.append(matrix[r][r])
        r -= 1
        
        # Move left along the bottom row (if there's a row remaining)
        if top <= bottom:
            for c in range(r, l - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
        
        # Move up along the left column (if there's a column remaining)
        if l <= r:
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][l])
            l += 1
    
    return res
