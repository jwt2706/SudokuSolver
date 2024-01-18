# Sudoku

## Overview

This is a simple Python Sudoku game with a built in autosolver. Sudoku is a logic-based puzzle game where the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contains all of the digits from 1 to 9.

The solver included in the game uses a backtracking algorithm to find a solution to the Sudoku puzzle. It starts by finding an empty cell in the grid and tries numbers from 1 to 9. If a number is valid for the current cell, it places the number and recursively attempts to solve the remaining empty cells. If a solution is found, it returns `True`, and if no solution is found, it backtracks and tries a different number. The solver repeats this process until the puzzle is solved or all possibilities are exhausted.

## Usage

To use the Sudoku solver, you can run the provided Python script. The script will generate a new Sudoku board and prompt the user to play or solve the board.

```
-------NEW-GAME-------
Original Sudoku board:
5 0 0 | 0 0 0 | 0 0 0
0 7 4 | 2 0 0 | 0 0 0
0 8 0 | 0 0 0 | 0 3 0
- - - - - - - - - - - -
0 6 0 | 0 0 0 | 4 0 3
4 0 7 | 0 0 0 | 0 0 0
0 0 0 | 0 0 3 | 0 0 6
- - - - - - - - - - - -
0 0 0 | 0 0 0 | 0 0 0
0 0 0 | 0 5 0 | 6 0 0
0 0 0 | 6 0 0 | 0 0 0

Do you want to play (p) or get the board solved (s)? Default is solving.
```

If you choose to play (`p`), you will be prompted to enter the row, column, and number to place in the Sudoku board. The program will check if the move is valid and update the board accordingly. If you solve the entire Sudoku board, you will see a congratulatory message.

If you choose to get the board solved (`s`), the program will attempt to solve the Sudoku board and display the solution.

After each game or solution, you will be asked if you want to play again. Entering `y` will generatea new Sudoku board, and entering `n` will end the program.

## Docs

### solve_sudoku(board)

This function is the main solver function that takes a Sudoku board as input and returns a Boolean value indicating whether a solution was found (`True`) or not (`False`).

**Parameters:**

- `board`: A 9x9 list representing the Sudoku board. Each cell in the grid is represented by an integer. Empty cells are denoted by the value `0`.

**Returns:**

- `True` if a solution is found, `False` otherwise.

### is_board_full(board)

This function checks if the Sudoku board is completely filled with numbers.

**Parameters:**

- `board`: A 9x9 list representing the Sudoku board.

**Returns:**

- `True` if the board is full, `False` otherwise.

### is_valid(board, num, pos)

This function checks if a number can be placed in a given position on the Sudoku board without violating the Sudoku rules.

**Parameters:**

- `board`: A 9x9 list representing the Sudoku board.
- `num`: The number to be checked.
- `pos`: A tuple `(row, col)` representing the position where the number is to be placed.

**Returns:**

- `True` if the number can be placed in the given position, `False` otherwise.

### find_empty_cell(board)

This function finds the next empty cell on the Sudoku board.

**Parameters:**

- `board`: A 9x9 list representing the Sudoku board.

**Returns:**

- A tuple `(row, col)` representing the position of the next empty cell, or `None` if there are no empty cells left.

### print_board(board)

This function prints the Sudoku board in a human-readable format.

**Parameters:**

- `board`: A 9x9 list representing the Sudoku board.

### generate_board()

This function generates a new Sudoku board with a random number of empty spots for the user to play.

**Returns:**

- A 9x9 list representing the generated Sudoku board.

