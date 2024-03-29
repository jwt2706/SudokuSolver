# Sudoku

## Overview

This is a simple Python Sudoku game with a built in autosolver. Sudoku is a logic-based puzzle game where the objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contains all of the digits from 1 to 9.

The solver included in the game uses a backtracking algorithm to find a solution to the Sudoku puzzle. It starts by finding an empty cell in the grid and tries numbers from 1 to 9. If a number is valid for the current cell, it places the number and recursively attempts to solve the remaining empty cells. If a solution is found, it returns `True`, and if no solution is found, it backtracks and tries a different number. The solver repeats this process until the puzzle is solved or all possibilities are exhausted.

## Usage

To use the Sudoku solver, you can run `sudoku.py`. The script will generate a new Sudoku board and prompt the user to play or solve the board.

```
Original Sudoku board:
1 2 3 | 0 5 0 | 0 8 9
0 5 6 | 7 0 9 | 1 2 3
7 8 9 | 1 0 0 | 0 0 6
- - - - - - - - - - - -
2 1 4 | 3 0 5 | 8 9 7
0 0 5 | 8 0 0 | 2 1 4
8 0 0 | 0 0 0 | 3 6 0
- - - - - - - - - - - -
0 0 1 | 0 4 2 | 9 0 8
6 0 2 | 9 7 0 | 5 3 0
9 7 0 | 5 0 1 | 6 0 2

Do you want to play (p) or get the board solved (s)? Default is solving.
```
Here is an example if the user selected to autosolve the board:
```
Solving Sudoku...
Sudoku solved:
1 2 3 | 4 5 6 | 7 8 9
4 5 6 | 7 8 9 | 1 2 3
7 8 9 | 1 2 3 | 4 5 6
- - - - - - - - - - - -
2 1 4 | 3 6 5 | 8 9 7
3 6 5 | 8 9 7 | 2 1 4
8 9 7 | 2 1 4 | 3 6 5
- - - - - - - - - - - -
5 3 1 | 6 4 2 | 9 7 8
6 4 2 | 9 7 8 | 5 3 1
9 7 8 | 5 3 1 | 6 4 2
```

If you choose to play (`p`), you will be prompted to enter the row, column, and number to place in the Sudoku board. The program will check if the move is valid and update the board accordingly. If you solve the entire Sudoku board, you will see a congratulatory message.

If you choose to get the board solved (`s`), as demonstrated above, the program will attempt to solve the Sudoku board and display the solution.
