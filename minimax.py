import board as bd
import sys
import random

# max corresponds to player1 winning, min corresponds to p1 losing
X_WIN = 10
X_LOSE = -10
TIE = 0

# higher moves left is a better win. Intuition is to prioritize winning methods
# that take less steps. Later think of extending losing to take longer maybe?

# TODO: Different Levels of AI


def max_helper(cur_score, cur_mv, max_val, max_mv):
    if cur_score >= max_val:
        max_val = cur_score
        max_mv = cur_mv
    return (max_val, max_mv)


# max_move(board, diff, moves_left) is a tuple [(a,b)] where [a] is > 0 if the game is
# winnable by player 1, 0 if tie, and <0 otherwise. [b] is the move that will
# lead to that result

def max_move(board, diff, moves_left):
    max_val = -sys.maxsize - 1
    max_mv = None
    next_moves = bd.possible_moves(board)
    rand_roll = random.randint(1, 100)
    if rand_roll <= diff:
        return (max_val, random.choice(next_moves))
    for mv in next_moves:
        bd.place_piece(board, mv, True)
        cur_val = None
        if bd.check_win(board, mv, True):
            cur_val = X_WIN + moves_left
        elif bd.check_win(board, mv, False):
            cur_val = X_LOSE + moves_left
        elif moves_left == 1:
            cur_val = TIE
        else:
            cur_val = min_move(board, 0, moves_left - 1)[0]
        max_val, max_mv = max_helper(cur_val, mv, max_val, max_mv)
        bd.remove_piece(board, mv)
    return (max_val, max_mv)


def min_helper(cur_score, cur_mv, min_val, min_mv):
    if cur_score <= min_val:
        min_val = cur_score
        min_mv = cur_mv
    return (min_val, min_mv)
# min_move(board, diff, moves_left) is a tuple [(a,b)] where [a] is > 0 if the game is
# winnable by player 2, 0 if tie, and < 0 otherwise. [b] is the move that will
# lead to that result


def min_move(board, diff, moves_left):
    min_val = sys.maxsize
    min_mv = None
    next_moves = bd.possible_moves(board)
    rand_roll = random.randint(1, 100)
    if rand_roll <= diff:
        return (min_val, random.choice(next_moves))
    for mv in next_moves:
        bd.place_piece(board, mv, False)
        cur_val = None
        if bd.check_win(board, mv, False):
            cur_val = X_LOSE - moves_left
        elif bd.check_win(board, mv, True):
            cur_val = X_WIN - moves_left
        elif moves_left == 1:
            cur_val = TIE
        else:
            cur_val = max_move(board, 0, moves_left - 1)[0]
        min_val, min_mv = min_helper(cur_val, mv, min_val, min_mv)
        bd.remove_piece(board, mv)
    return (min_val, min_mv)

# for all valid moves, check the minimax value. set the best move pointer to be
# the one with the highest minimax value


def best_move(board, is_max, diff, moves_left):
    res = max_move(board, diff, moves_left) if is_max else min_move(
        board, diff, moves_left)
    return res[1]
