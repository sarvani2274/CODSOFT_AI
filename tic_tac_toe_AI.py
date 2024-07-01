import math
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    if winner == "O":
        return 10 - depth
    if check_draw(board):
        return 0
    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def get_best_move(board):
    best_move = None
    best_value = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_value = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move
    
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        while True:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Invalid move. Try again.")
        print_board(board)
        if check_winner(board):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        print("AI is making a move...")
        best_move = get_best_move(board)
        board[best_move[0]][best_move[1]] = "O"
        print_board(board)
        if check_winner(board):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
if __name__ == "__main__":
    play_game()