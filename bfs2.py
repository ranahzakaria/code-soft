import random

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

# Define a function for the computer's turn using BFS
def computer_turn(): 
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = "-"

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

# Minimax algorithm with BFS for computer's move
def minimax(board, depth, is_maximizing):
    result = check_game_over()

    if result == "O":
        return 1
    elif result == "X":
        return -1
    elif result == "tie":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = "-"
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
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
            position = int(input("Enter your move (1-9): ")) - 1
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