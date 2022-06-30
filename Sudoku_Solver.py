# Andrew Daur - Python Recursion exercise.
# This entire program is solving a soduko using backtracking.
from pprint import pprint


# Find the open spaces on the board. (represented by -1)
def empty_space(puzzle):
    # checking each row and checking each column
    for r in range(9):
        for c in range(9):  # range of 9 takes 0-8
            if puzzle[r][c] == -1:
                return r, c
    # return (None, None) when there is no more empty spaces. (-1 is the empty space)
    return None, None


# Figureing out whether or not the row, and column are valid.
def validate(puzzle, guess, row, col):
    row_val = puzzle[row]
    if guess in row_val:
        return False  # In our row

    # Taking puzzle and indexing into i, and then within that row, index into "col" for i in range 9.
    col_val = [puzzle[i][col] for i in range(9)]
    if guess in col_val:
        return False  # In our column

    # Reminder of where in the 3x3 grid we are. Iterating over 3 values.
    row_start = (row // 3) * 3  # Returning only whole numbers
    col_start = (col // 3) * 3  # Returning only whole numbers

    # iterating through all 3 rows and columns.
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False  # Guess is inside the matrix/puzzle

    return True  # valid puzzle.


def solve_sudoku(puzzle):
    # Finding the next empty space is the first step, and finding the combination that fits
    row, col = empty_space(puzzle)

    # Puzzle is solves if row is None.
    if row is None:
        return True

    # Placing the number correctly
    for guess in range(1, 10):  #
        # If these values are valid guesses
        if validate(puzzle, guess, row, col):
            # placing the guess into the matrix. Mutate the puzzle array
            puzzle[row][col] = guess
            # Continue to recursizely call the function, and return True when puzzle is solved.
            if solve_sudoku(puzzle):
                return True

        # Backtracking. We will reset, and try some more numbers. Resetting the value at this row and Column.
        # This continues until the computer find the correct combination
        puzzle[row][col] = -1

    # If the sudoku problem isn't solvable, the program returns False.
    return False


# This is an example sudoku puzzle. Insert any puzzle to get your answer.
if __name__ == '__main__':
    example_board = [
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, -1, -1,   3, 4, -1,   1, -1, -1],
        [-1, -1, 1,   -1, 6, -1,   2, -1, -1],

        [3, -1, 4,   9, 2, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 9],
        [-1, -1, -1,   -1, -1, -1,   5, -1, 6],

        [4, -1, -1,   6, 8, -1,   -1, -1, -1],
        [1, 2, -1,   -1, -1, 4,   9, -1, -1],
        [-1, 8, -1,   -1, -1, -1,   -1, 7, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
