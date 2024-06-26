import random
import time

# Set up the game board as a list
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

# Define a function to print the game board
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != "-":
            return board[i]

    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != "-":
            return board[i]

    if board[0] == board[4] == board[8] != "-":
        return board[0]
    
    if board[2] == board[4] == board[6] != "-":
        return board[2]

    # Check for a tie
    if "-" not in board:
        return "tie"
    
    return None

# Define a function for the computer's turn using IDDFS
def computer_turn():
    start_time = time.time()
    depth_limit = 1

    while True:
        best_score, best_move = iddfs(board, depth_limit, start_time)
        if best_move is not None:
            board[best_move] = "O"
            return
        depth_limit += 1

# Iterative Deepening Depth-First Search (IDDFS)
def iddfs(board, depth_limit, start_time):
    best_score = -float("inf")
    best_move = None
    is_maximizing = True

    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = recursive_dls(board, depth_limit, is_maximizing, start_time)
            board[i] = "-"

            if score > best_score:
                best_score = score
                best_move = i

    return best_score, best_move

# Recursive Depth-Limited Search (DLS) for IDDFS
def recursive_dls(board, depth_limit, is_maximizing, start_time):
    result = check_game_over()

    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "tie" or depth_limit == 0:
        return 0

    if time.time() - start_time > 1:
        return 0  # Timeout, return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = recursive_dls(board, depth_limit - 1, False, start_time)
                board[i] = "-"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = recursive_dls(board, depth_limit - 1, True, start_time)
                board[i] = "-"
                best_score = min(score, best_score)
        return best_score

# Define the main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the computer is O.")
    print("Enter your move as a number from 1 to 9 (top-left is 1, bottom-right is 9).")
    print_board()
    current_player = "X"
    game_over = False

    while not game_over:
        if current_player == "X":
            position = int(input("Enter your move (1-9): ") )- 1
            if 0 <= position < 9 and board[position] == "-":
                board[position] = "X"
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("Computer's turn:")
            computer_turn()

        print_board()
        game_result = check_game_over()

        if game_result == "X":
            print("You win!")
            game_over = True
        elif game_result == "O":
            print("Computer wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "X" if current_player == "O" else "O"

# Start the game
play_game()