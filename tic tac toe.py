# Tic Tac Toe Game

def print_board(board):
    """Prints the current state of the board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if the given player has won the game."""
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def get_move():
    """Gets a move from the player."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Move must be between 1 and 9.")
                continue
            return move
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def update_board(board, move, player):
    """Updates the board with the player's move."""
    row, col = divmod(move, 3)
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

def play_game():
    """Main function to play the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        move = get_move()
        
        if not update_board(board, move, current_player):
            print("This cell is already taken. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        3
        if is_board_full(board):
            print_board(board)
            print("The game is a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
    

