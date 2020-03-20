BOARD_WIDTH = 3
WIN = 1
LOSE = -1
TIE = 0

game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
is_won = False
is_tie = False
moves_remaining = BOARD_WIDTH ** 2

# print_board(board) converts the board [board] into a readable message in the
# console


def print_board(board):
    for r in board:
        for elmnt in r:
            print("| %s" % elmnt, end=" ")
        print()

# is_empty_cell(board, pos) is true if the tuple [pos] is an empty cell of
# board [board], false otherwise.


def is_empty_cell(board, pos):
    r, c = pos[0], pos[1]
    res = board[r][c] == ' '
    return res

# is_valid(board, pos) is true if the given tuple [pos] is a valid position of
# the board [board], false otherwise.


def is_valid(board, pos):
    correct_dimension = ((0 <= pos[0]) and (pos[0] < 3)
                         and (0 <= pos[1]) and (pos[1] < 3))
    return correct_dimension and is_empty_cell(board, pos)

# get_input() translates user input string to a valid move position tuple


def get_input(board):
    loc = input("Input row as 'r_number,c_number': ")
    loc_list = loc.split(',')
    if len(loc_list) != 2:
        print("Not a valid move, try again.")
        return get_input(board)
    r, c = int(loc_list[0]), int(loc_list[1])
    pos = (r, c)
    if not (is_valid(board, pos)):
        print("Not a valid move, try again.")
        return get_input(board)
    return pos

# place_piece(board, move, is_player1) fills in cell at location [move] on board
# [board] with the correct piece by either player1 or player2, specified by
# [is_player1]


def place_piece(board, move, is_player1):
    piece = 'X' if is_player1 else 'O'
    r, c = move[0], move[1]
    board[r][c] = piece

# TODO: Document check_win


def check_win(board, move, is_player1):
    col, row, diag, right_diag = 0, 0, 0, 0
    x, y = move[0], move[1]
    player = 'X' if is_player1 else 'O'
    for i in range(3):
        col += 1 if board[x][i] == player else 0
        row += 1 if board[i][y] == player else 0
        diag += 1 if board[i][i] == player else 0
        right_diag += 1 if board[i][2-i] == player else 0
    if (col == 3) or (row == 3) or (diag == 3) or (right_diag == 3):
        return True
    return False

# TODO: Document game_loop


def game_loop(is_player1, board):
    global is_won, is_tie, moves_remaining
    while not (is_won or is_tie):
        print_board(board)
        pos = get_input(board)
        place_piece(board, pos, is_player1)
        moves_remaining = moves_remaining - 1
        is_won = check_win(board, pos, is_player1)
        is_tie = (not is_won) and (moves_remaining == 0)
        if (is_won or is_tie):
            break
        is_player1 = not is_player1
    print_board(board)
    if is_tie:
        print("TIE!")
    else:
        player = 1 if is_player1 else 2
        print("Player %d is the winner!" % player)


def main():
    is_p1 = True
    game_loop(is_p1, game_board)


if __name__ == "__main__":
    main()
