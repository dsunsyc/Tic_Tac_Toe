BOARD_WIDTH = 3
WIN = 1
LOSE = -1
TIE = 0

game_board = [['', '', ''], ['', '', ''], ['', '', '']]
is_won = False


def print_board(board):
    for r in board:
        for elmnt in r:
            print("| %s" % elmnt, end=" ")
        print()


def get_input():
    loc = input("Input row, column: ")
    return False


def game_loop(isPlayer):
    if is_won:
        print("%s won!")
    # if isPlayer:

    # else:
    #   # check if there are more spaces that can be filled
    #   loc =


def main():
    game_loop()


if __name__ == "__main__":
    main()
