def spiralMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    res = []
    
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1

    while top <= bottom and left <= right:

        # Traverse top row
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1

        # Traverse right column
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1

        # Traverse bottom row and make sure to check second row exists
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

        # Traverse left column and make sure to check that top column exists
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

    return res
