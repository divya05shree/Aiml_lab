def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the current player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    """Checks if the board is full (a draw)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)
        
        try:
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
            
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid input. Row and column must be between 0 and 2. Try again.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            
            board[row][col] = current_player
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                break
                
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"
            
        except ValueError:
            print("Invalid input. Please enter a number.")
            
if __name__ == "__main__":
    tic_tac_toe()
