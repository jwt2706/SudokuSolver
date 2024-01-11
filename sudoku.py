import random
 
def solve_sudoku(board):
    # Find an empty cell
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    # Try numbers from 1 to 9
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            # Undo the current cell if the solution is not valid
            board[row][col] = 0
    return False
 
def is_board_full(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return False
    return True

def is_valid(board, num, pos):
    if board[pos[0]][pos[1]] != 0:
        return False
    # Check row
    for col in range(9):
        if board[pos[0]][col] == num and pos[1] != col:
            return False
    # Check column
    for row in range(9):
        if board[row][pos[1]] == num and pos[0] != row:
            return False
    # Check box
    box_row = pos[0] // 3
    box_col = pos[1] // 3
    for row in range(box_row * 3, box_row * 3 + 3):
        for col in range(box_col * 3, box_col * 3 + 3):
            if board[row][col] == num and (row, col) != pos:
                return False
    return True

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")
                
def generate_board():
    # Generate an empty Sudoku board
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    # Remove some numbers to create empty spots for the user to play
    empty_spots = random.randint(40, 60)
    for _ in range(empty_spots):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        board[row][col] = 0
    return board

while True:
    board = generate_board()
    print("-------NEW-GAME-------")
    print("Original Sudoku board:")
    print_board(board)
    choice = input("\nDo you want to play (p) or get the board solved (s)? Default is solving.").upper()
    if choice == "P":
         while True:
            print_board(board)
            row = int(input("\nEnter the row number (1-9): ")) - 1
            col = int(input("Enter the column number (1-9): ")) - 1
            num = int(input("Enter the number (1-9) to place: "))

            if is_valid(board, num, (row, col)):
                board[row][col] = num
            else:
                print("Invalid move. Please try again.\n")

            if is_board_full(board):
                print("\nCongratulations! You solved the Sudoku!")
                break
    else:
        print("\nSolving Sudoku...\n")
        if solve_sudoku(board):
            print("Sudoku solved:")
            print_board(board)
        else:
            #This case shouldn't be possible.. but you never know
            print("No solution exists for the given Sudoku board.")
    again = input("Play again? (y or n): ").upper()
    if (again == "N"):
        print("bye bye.")
        break