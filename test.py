#nothing, just to test the function
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]  # Column win
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Main diagonal win
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Opposite diagonal win
    
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}, enter your move (row and column 0-2): ")
        
        try:
            row, col = map(int, input().split())
            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue
            board[row][col] = player
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column as two numbers between 0 and 2.")
            continue
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        turn += 1

if __name__ == "__main__":
    tic_tac_toe()
