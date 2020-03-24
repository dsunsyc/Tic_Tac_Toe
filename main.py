import board as bd
import minimax

BOARD_WIDTH = 3

game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
is_won = False
is_tie = False
moves_remaining = BOARD_WIDTH ** 2


def reset():
    global game_board, is_won, is_tie, moves_remaining
    game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    is_won, is_tie = False, False
    moves_remaining = 9


def get_players():
    while True:
        try:
            num_players = int(input("1 or 2 players: "))
            if num_players != 1 and num_players != 2:
                raise ValueError
            return num_players
        except ValueError:
            print("Invalid input. Try again.")


def get_diff():
    diff = input("Input difficulty (easy, medium, impossible): ")
    if diff != "easy" and diff != "medium" and diff != "impossible":
        print("Invalid input. Try again.")
        return get_diff()
    if diff == "easy":
        return 100
    elif diff == "medium":
        return 50
    else:
        return 0

# TODO: Document game_loop


def game_loop(board, is_player1, use_bot, diff):
    global is_won, is_tie, moves_remaining
    while not (is_won or is_tie):
        print("Moves left: %d" % moves_remaining)
        pos = None
        if (not is_player1) and use_bot:
            pos = minimax.best_move(board, False, diff, moves_remaining)
        else:
            bd.print_board(board)
            pos = bd.get_input(board)
        bd.place_piece(board, pos, is_player1)
        moves_remaining = moves_remaining - 1
        is_won = bd.check_win(board, pos, is_player1)
        is_tie = (not is_won) and (moves_remaining == 0)
        if (is_won or is_tie):
            break
        is_player1 = not is_player1
    bd.print_board(board)
    if is_tie:
        print("TIE!")
    else:
        player = 1 if is_player1 else 2
        print("Player %d is the winner!" % player)


# if input for number of players is 2, then shouldn't ask for difficulty


def main():
    use_bot = get_players() == 1
    diff = get_diff() if use_bot else 0
    is_p1 = True
    game_loop(game_board, is_p1, use_bot, diff)
    is_replay = input("Play again (y/n)?: ")
    if is_replay == 'y':
        reset()
        main()


if __name__ == "__main__":
    main()
