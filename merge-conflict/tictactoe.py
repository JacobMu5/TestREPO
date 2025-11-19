def print_board(board):
    """
    Prints the current state of the board.
    """
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    """
    Checks if the specified player has won.
    Returns True if there is a winner, False otherwise.
    """
    # Winning combinations: rows, columns, diagonals
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_board_full(board):
    """
    Checks if the board is full (a draw).
    """
    return " " not in board

def get_valid_input(board):
    """
    Prompts the user for a move until a valid one is received.
    """
    while True:
        try:
            move = int(input("Choose a position (1-9): "))
            if 1 <= move <= 9:
                if board[move - 1] == " ":
                    return move - 1
                else:
                    print("That spot is already taken. Try again.")
            else:
                print("Please choose a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    """
    Main game loop.
    """
    print("Welcome to Tic-Tac-Toe!")
    print("Player 1 is X, Player 2 is O")
    
    # Initialize a list of 9 spaces
    board = [" " for _ in range(9)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get move and update board
        move_index = get_valid_input(board)
        board[move_index] = current_player
        
        # Check for win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()