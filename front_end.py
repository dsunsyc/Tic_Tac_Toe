from tkinter import *
import minimax
import board

SQUARE_SIZE = 600
CELL_SIZE = SQUARE_SIZE/3
SYMBOL_SIZE = .5
SYMBOL_WIDTH = SQUARE_SIZE/12

X_COLOR = '#1fceff'
O_COLOR = '#ff33be'
BG_COLOR = 'white'
TIE_COLOR = '#8fd18e'
FONT = 'David'

MENU_STATE = 0
O_TURN_STATE = 1
X_TURN_STATE = 2
END_STATE = 3


class Game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.canvas = Canvas(height=SQUARE_SIZE,
                             width=SQUARE_SIZE, bg=BG_COLOR)

        self.canvas.pack()

        self.bind('<Escape>', self.quit)
        self.bind('<Button-1>', self.on_click)

        self.gamestate = MENU_STATE
        self.title_screen()

        self.game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.first_isX = True

        self.is_won = False
        self.is_tie = False

        self.is_multi = False
        self.diff = 0

        self.moves_remaining = 9

    # def two_player(self):
    #     self.reset()
    #     # self.first_isX = not self.first_isX
    #     self.gamestate = X_TURN_STATE  # if self.first_isX else O_TURN_STATE
    #     self.is_multi = True

    def title_screen(self):
        # TODO:
        self.canvas.delete('all')  # clears board
        self.canvas.create_rectangle(
            0, 0, SQUARE_SIZE, SQUARE_SIZE, outline='')

        self.canvas.create_rectangle(
            int(SQUARE_SIZE/15), int(SQUARE_SIZE/15),
            int(SQUARE_SIZE*14/15), int(SQUARE_SIZE*14/15),
            width=int(SQUARE_SIZE/20),
            outline=X_COLOR)

        self.canvas.create_rectangle(
            int(SQUARE_SIZE/10), int(SQUARE_SIZE/10),
            int(SQUARE_SIZE*9/10), int(SQUARE_SIZE*9/10),
            fill=X_COLOR,
            outline='')

        self.canvas.create_text(
            SQUARE_SIZE/2,
            SQUARE_SIZE/3,
            text='TIC TAC TOE', fill='white',
            font=('Franklin Gothic', int(-SQUARE_SIZE/12), 'bold'))

        self.canvas.create_text(
            int(SQUARE_SIZE/2),
            int(SQUARE_SIZE/2.5),
            text='[click to play]', fill='white',
            font=('Franklin Gothic', int(-SQUARE_SIZE/25)))

        # b_diff = Button(self.canvas, text='Diff_Test', bg='white',
        #                 activebackground='dodger blue',
        #                 command=lambda: b_diff.destroy())
        # b_diff.place(relx=.25, rely=.45, relwidth=.5, relheight=.3)

        # b_p1 = Button(self.canvas, text='1 Player', bg='white',
        #               activebackground='dodger blue',
        #               command=lambda: b_p1.destroy())
        # b_p2 = Button(self.canvas, text='2 Players',
        #               bg='white', activebackground="tomato",
        #               command=self.two_player())
        # b_p1.place(relx=.25, rely=.45, relwidth=.25, relheight=.3)
        # b_p2.place(relx=.5, rely=.45, relwidth=.25, relheight=.3)

    def reset(self):
        self.canvas.delete('all')
        self.game_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.moves_remaining = 9
        self.is_won = False
        self.is_tie = False
        self.canvas.create_line(SQUARE_SIZE/3, 0, SQUARE_SIZE /
                                3, SQUARE_SIZE, width=4)
        self.canvas.create_line(2*SQUARE_SIZE/3, 0, 2*SQUARE_SIZE /
                                3, SQUARE_SIZE, width=4)
        self.canvas.create_line(0, SQUARE_SIZE/3, SQUARE_SIZE,
                                SQUARE_SIZE/3, width=4)
        self.canvas.create_line(0, 2*SQUARE_SIZE/3, SQUARE_SIZE,
                                2*SQUARE_SIZE/3, width=4)

    def game_over_screen(self, result):
        self.canvas.delete('all')
        if result == 2:
            win_text = 'X Wins'
            win_color = X_COLOR
        elif result == 1:
            win_text = 'O Wins'
            win_color = O_COLOR
        else:
            win_text = "Tie"
            win_color = TIE_COLOR
        self.canvas.create_rectangle(
            0, 0, SQUARE_SIZE, SQUARE_SIZE, fill=win_color, outline='')
        self.canvas.create_text(int(SQUARE_SIZE/2), int(SQUARE_SIZE/2),
                                text=win_text, fill='white',
                                font=('Franklin Gothic', int(-SQUARE_SIZE/6),
                                      'bold'))
        self.canvas.create_text(int(SQUARE_SIZE/2), int(SQUARE_SIZE/1.65),
                                text='[click to replay]', fill='white',
                                font=('Franklin Gothic', int(-SQUARE_SIZE/25)))
    # y represents the row, x represents the column

    def cell_to_pix(self, cell):
        r, c = cell
        y, x = r*CELL_SIZE + (CELL_SIZE/2), c*CELL_SIZE + (CELL_SIZE/2)
        return (y, x)

    # TODO: BE CAREFUL FOR THE TRANSLATION FROM COORDINATES TO BOARD LOCATION
    #       COORD (1,2) MEANS X = 1, Y = 2, WHICH BECOMES LOCATION [2][1]
    def pix_to_cell(self, pix):
        x = SQUARE_SIZE - 1 if pix[0] >= SQUARE_SIZE else pix[0]
        y = SQUARE_SIZE - 1 if pix[1] >= SQUARE_SIZE else pix[1]
        return (int(y/CELL_SIZE), int(x/CELL_SIZE))

    def draw_X(self, cell):
        """
        draw the X symbol at x, y in the grid
        """

        x, y = self.cell_to_pix(cell)
        delta = CELL_SIZE/2*SYMBOL_SIZE

        self.canvas.create_line(
            x-delta, y-delta,
            x+delta, y+delta,
            width=SYMBOL_WIDTH, fill=X_COLOR)

        self.canvas.create_line(
            x+delta, y-delta,
            x-delta, y+delta,
            width=SYMBOL_WIDTH, fill=X_COLOR)

    def draw_O(self, cell):
        """
        draw an O symbol at x, y in the grid
        note : a big outline value appears to cause a visual glitch in tkinter
        """
        x, y = self.cell_to_pix(cell)
        delta = 1.5*CELL_SIZE/2*SYMBOL_SIZE
        self.canvas.create_oval(
            x-delta, y-delta,
            x+delta, y+delta,
            fill=O_COLOR, outline="")
        self.canvas.create_oval(
            x-delta/3, y-delta/3,
            x+delta/3, y+delta/3,
            fill=BG_COLOR, outline="")

    def has_won(self, move):
        is_player1 = 1 if self.gamestate == X_TURN_STATE else 0
        return board.check_win(self.game_board, move, is_player1)

    def has_tie(self):
        return self.moves_remaining == 0 and not self.is_won

    def new_move(self, cell):
        is_player1 = 1 if self.gamestate == X_TURN_STATE else 0
        board.place_piece(self.game_board, cell, is_player1)
        if is_player1:
            self.draw_X(cell)
        else:
            self.draw_O(cell)

    def on_click(self, event):
        # TODO:
        c, r = self.pix_to_cell((event.x, event.y))
        if self.gamestate == END_STATE:
            self.reset()
            self.gamestate = MENU_STATE
            self.title_screen()
        elif self.gamestate == MENU_STATE:
            self.reset()
            self.first_isX = not self.first_isX
            self.gamestate = X_TURN_STATE if self.first_isX else O_TURN_STATE
        elif ((self.gamestate == X_TURN_STATE or
               self.gamestate == O_TURN_STATE) and
              board.is_valid(self.game_board, (r, c))):
            cur_player = 1 if self.gamestate == X_TURN_STATE else 0
            # self.new_move(cur_player, (r, c))
            self.new_move((r, c))
            self.moves_remaining -= 1
            # if self.has_won(cur_player, (r, c)):
            if self.has_won((r, c)):
                self.is_won = True
                self.gamestate = END_STATE
                self.game_over_screen(cur_player+1)
            elif self.has_tie():
                self.gamestate = END_STATE
                self.game_over_screen(0)
            else:
                self.gamestate = int(not (self.gamestate - 1)) + 1

    def quit(self, event):
        self.destroy()


# def raise_frame(frame):
#     frame.tkraise()


# def get_pos(event):
#     x, y = event.x, event.y
#     r, c = int(event.x/3), int(event.y/3)
#     print("clicked at", r, c)
#     return (r, c)


# def nextMove(event):
#     if not (is_won or is_tie):
#         mv = get_pos(event)
#         print("hi")


# def start_game(event, is_p1, use_bot):
#     raise_frame(event)
#     nextMove(event)


# root = Tk()

# root.title("Tic-Tac-Toe")

# canvas = Canvas(root, height=HEIGHT, width=WIDTH)
# canvas.pack()


# f1 = Frame(root, bg=BACKGROUND)
# f2 = Frame(root, bg=BACKGROUND)

# f1.place(relwidth=1, relheight=1)
# f2.place(relwidth=1, relheight=1)

# c1 = Canvas(f2, height=HEIGHT, width=WIDTH)
# c1.pack()
# c1.create_line(WIDTH/3, 0, WIDTH/3, SQUARE_HEIGHT, width=4)
# c1.create_line(2*WIDTH/3, 0, 2*WIDTH/3, SQUARE_HEIGHT, width=4)
# c1.create_line(0, SQUARE_HEIGHT/3, WIDTH, SQUARE_HEIGHT/3, width=4)
# c1.create_line(0, 2*SQUARE_HEIGHT/3, WIDTH, 2*SQUARE_HEIGHT/3, width=4)

# c1.bind("<Button-1>", get_pos)
# c1.pack()


# l_intro = Label(f1, text='Welcome to Tic-Tac-Toe!', font=FONT)
# b_p1 = Button(f1, text='1 Player', command=lambda: raise_frame(f2))
# # start game with two players
# b_p2 = Button(f1, text='2 Players', command=lambda: start_game(f2, True, True))
# l_intro.place(relx=.25, rely=.2, relwidth=.5, relheight=.2)
# b_p1.place(relx=.25, rely=.45, relwidth=.25, relheight=.2)
# b_p2.place(relx=.5, rely=.45, relwidth=.25, relheight=.2)

# Label(f2, text='FRAME 2').place(relx=.3, rely=.9)
# Button(f2, text='Go to frame 1', command=lambda: raise_frame(
#     f1)).place(relx=.5, rely=.9)

# Label(f3, text='FRAME 3').pack()
# Button(f3, text='Go to frame 1', command=lambda: raise_frame(f1)).pack()

# raise_frame(f1)
# root.mainloop()


def main():
    root = Game()
    root.mainloop()


main()
