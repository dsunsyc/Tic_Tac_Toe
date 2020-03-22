import board as bd
import sys

# max corresponds to player1 winning, min corresponds to p1 losing
X_WIN = 100
X_LOSE = -100
TIE = 0

# higher moves left is a better win. Intuition is to prioritize winning methods
# that take less steps. Later think of extending losing to take longer maybe?

# max_move(board, moves_left) is a tuple [(a,b)] where [a] is > 0 if the game is
# winnable by player 1, 0 if tie, and <0 otherwise. [b] is the move that will
# lead to that result


def max_move(board, moves_left):
    max_val = -sys.maxsize - 1
    max_mv = None
    next_moves = bd.possible_moves(board)
    # need to consider the no possible move situation (full board state) CHECK FOR NONE
    for mv in next_moves:
        bd.place_piece(board, mv, True)
        # bd.print_board(board)
        if bd.check_win(board, mv, True):
            if X_WIN > max_val:
                max_val = X_WIN
                max_mv = mv
        elif bd.check_win(board, mv, False):
            if X_LOSE > max_val:
                max_val = X_LOSE
                max_mv = mv
        elif moves_left == 1:
            if TIE > max_val:
                max_val = TIE
                max_mv = mv
        else:
            min_tple = min_move(board, moves_left - 1)
            if min_tple[0] > max_val:
                max_val = min_tple[0]
                max_mv = min_tple[1]
        bd.remove_piece(board, mv)
    return (max_val, max_mv)


# min_move(board, moves_left) is a tuple [(a,b)] where [a] is > 0 if the game is
# winnable by player 2, 0 if tie, and < 0 otherwise. [b] is the move that will
# lead to that result
# P2 CURRENTLY sometimes WINS
def min_move(board, moves_left):
    min_val = sys.maxsize
    min_mv = None
    next_moves = bd.possible_moves(board)
    for mv in next_moves:
        bd.place_piece(board, mv, False)
        # bd.print_board(board)
        if bd.check_win(board, mv, False):
            # print("I made it to p2 winning")
            if X_LOSE < min_val:
                min_val = X_LOSE
                min_mv = mv
        elif bd.check_win(board, mv, True):
            # print("I made it to p1 winning")
            if X_WIN < min_val:
                min_val = X_WIN
                min_mv = mv
        elif moves_left == 1:
            if TIE < min_val:
                min_val = TIE
                min_mv = mv
        else:
            # print("I made it to the else")
            max_tple = max_move(board, moves_left - 1)
            if max_tple[0] < min_val:
                min_val = max_tple[0]
                min_mv = max_tple[1]
        bd.remove_piece(board, mv)
        # print("FOR DEBUGGING: min_val: %d" % min_val)
        # bd.print_board(board)
    return (min_val, min_mv)

# for all valid moves, check the minimax value. set the best move pointer to be
# the one with the highest minimax value


def best_move(board, is_max, moves_left):
    # if not is_max:
    #     # print("Is minimizer")
    res = max_move(board, moves_left) if is_max else min_move(
        board, moves_left)
    return res[1]
