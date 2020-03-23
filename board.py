# board module defines the methods for interacting and accessing the game_board


# print_board(board) converts the list, list [board] into a readable message in the
# console


def print_board(board):
    for r in board:
        for elmnt in r:
            print("| %s" % elmnt, end=" ")
        print()
    print()

# is_empty_cell(board, pos) is true if the tuple [pos] is an empty cell of
# list, list [board], false otherwise.


def is_empty_cell(board, pos):
    r, c = pos[0], pos[1]
    res = board[r][c] == ' '
    return res

# is_valid(board, pos) is true if the given tuple [pos] is a valid position of
# the list, list [board], false otherwise.


def is_valid(board, pos):
    correct_dimension = ((0 <= pos[0]) and (pos[0] < 3)
                         and (0 <= pos[1]) and (pos[1] < 3))
    return correct_dimension and is_empty_cell(board, pos)

# get_input() translates user input string to a valid move position tuple


def get_input(board):
    loc = input("Input row as 'r_number,c_number': ")
    new_loc = loc.replace(" ", "")
    loc_list = new_loc.split(',')
    try:
        r, c = int(loc_list[0]), int(loc_list[1])
    except ValueError:
        print("Not a valid move, try again.")
        return get_input(board)
    pos = (r, c)
    if not (is_valid(board, pos)):
        print("Not a valid move, try again.")
        return get_input(board)
    return pos

# place_piece(board, move, is_player1) fills in cell at location [move] on
# list, list [board] with the correct piece by either player1 or player2,
# specified by [is_player1]


def place_piece(board, move, is_player1):
    piece = 'X' if is_player1 else 'O'
    r, c = move[0], move[1]
    board[r][c] = piece

# remove_piece(board, move) sets the cell specified at coordinates [move] on
# the string list, list [board] to be ' '


def remove_piece(board, move):
    r, c = move[0], move[1]
    board[r][c] = ' '

# check_win(board, move, is_player1) returns True if the result of playing
# a piece at coordinates [move] on string list, list [board] by player specified
# by boolean [is_player1] is a win (3 of the same piece in a row) or False
# otherwise


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

# possible_moves(board) returns a list of int tuples representing possible next
# moves on string list, list [board]


def possible_moves(board):
    res = []
    for r in range(3):
        for c in range(3):
            if is_empty_cell(board, (r, c)):
                res.append((r, c))
    return res
