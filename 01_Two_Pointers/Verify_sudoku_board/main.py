from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    grid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                continue

            if num in row_sets[r]:
                return False
            if num in col_sets[c]:
                return False
            if num in grid_sets[r // 3][c // 3]:
                return False
            
            row_sets[r].add(num)
            col_sets[c].add(num)
            grid_sets[r // 3][c // 3].add(num)
            
    return True

def test_valid_empty_board():
    """Test with empty board (all zeros)"""
    board = [[0] * 9 for _ in range(9)]
    assert verify_sudoku_board(board) == True


def test_valid_partial_board():
    """Test with valid partial board"""
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    assert verify_sudoku_board(board) == True


def test_duplicate_in_row():
    """Test with duplicate number in row"""
    board = [[0] * 9 for _ in range(9)]
    board[0] = [1, 2, 3, 4, 5, 6, 7, 8, 1]
    assert verify_sudoku_board(board) == False


def test_duplicate_in_column():
    """Test with duplicate number in column"""
    board = [[0] * 9 for _ in range(9)]
    board[0][0] = 5
    board[8][0] = 5
    assert verify_sudoku_board(board) == False


def test_duplicate_in_grid():
    """Test with duplicate number in 3x3 grid"""
    board = [[0] * 9 for _ in range(9)]
    board[0][0] = 7
    board[2][2] = 7
    assert verify_sudoku_board(board) == False


def test_all_numbers_valid():
    """Test with single row containing all valid numbers"""
    board = [[0] * 9 for _ in range(9)]
    board[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert verify_sudoku_board(board) == True

test_valid_empty_board()
test_valid_partial_board()
test_duplicate_in_row()
test_duplicate_in_column()
test_duplicate_in_grid()
test_all_numbers_valid()