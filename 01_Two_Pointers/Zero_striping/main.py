from typing import List


def zero_striping_hash_sets(matrix: List[List[int]]) -> None:
    """
    Time Complexity: O(rows * cols)
    Space Complexity: (rows + cols)
    """
    
    if not matrix or not matrix[0]:
        return
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
            
    for r in range(rows):
        for c in range(cols):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0

def zero_striping(matrix: List[List[int]]) -> None:
    """
    Time Complexity:
    Space Complexity:
    """
    if not matrix or not matrix[0]:
        return None
    rows, cols = len(matrix), len(matrix[0])
    
    first_row_has_zero = False
    for c in range(cols):
        if matrix[0][c] == 0:
            first_row_has_zero = True
            break
    
    first_col_has_zero = False
    for r in range(rows):
       if matrix[r][0] == 0:
           first_col_has_zero = True
           break
    
    for r in range(1, rows):
       for c in range(1, cols):
           if matrix[r][c] == 0:
               matrix[0][c] = 0
               matrix[r][0] = 0

    for r in range(1, rows):
       for c in range(1, cols):
           if matrix[0][c] == 0 or matrix[r][0] == 0:
               matrix[r][c] = 0
    
    if first_row_has_zero:
        for c in range(cols):
            matrix[0][c] = 0
    if first_col_has_zero:
        for r in range(rows):
            matrix[r][0] = 0

matrix = [
    [1, 2, 3, 4, 5],
    [6, 0, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 0],
]

print(matrix)
zero_striping_hash_sets(matrix)
print(matrix)

matrix = [
    [0, 2, 3, 4, 5],
    [6, 0, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 0],
]

print(matrix)
zero_striping_hash_sets(matrix)
print(matrix)
