def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all(
        [board[i][2 - i] == player for i in range(3)]
    ):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    print_board(board)

    for _ in range(9):
        row = int(input("Enter row (0, 1, 2) for player " + players[current_player] + ": "))
        col = int(input("Enter column (0, 1, 2) for player " + players[current_player] + ": "))
        if board[row][col] != " ":
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = players[current_player]
        print_board(board)

        if check_win(board, players[current_player]):
            print("Player " + players[current_player] + " wins!")
            break

        current_player = (current_player + 1) % 2
    else:
        print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
