import board
import minimax
import main

import unittest


class TestBoardMethods(unittest.TestCase):

    def test_is_empty_cell(self):
        test_board_empty = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        test_board_full = [['X', 'O', 'O'], ['O', 'X', 'X'], ['X', 'X', '0']]
        for i in range(3):
            for j in range(3):
                self.assertTrue(board.is_empty_cell(test_board_empty, (i, j)))
        for i in range(3):
            for j in range(3):
                self.assertFalse(board.is_empty_cell(test_board_full, (i, j)))

    def test_is_valid(self):
        test_board_empty = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        test_board_full = [['X', 'O', 'O'], ['O', 'X', 'X'], ['X', 'X', '0']]
        for i in range(3):
            for j in range(3):
                self.assertTrue(board.is_valid(test_board_empty, (i, j)))
        for i in range(3):
            for j in range(3):
                self.assertFalse(board.is_valid(test_board_full, (i, j)))
        self.assertFalse(board.is_valid(test_board_empty, (-1, -1)))
        self.assertFalse(board.is_valid(test_board_full, (4, 4)))
        self.assertFalse(board.is_valid(test_board_empty, (-100, 0)))
        self.assertFalse(board.is_valid(test_board_empty, (2, 1000)))

    def test_alter_board(self):
        test_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        board.place_piece(test_board, (0, 0), True)
        self.assertTrue(test_board[0][0] == 'X')
        board.remove_piece(test_board, (0, 0))
        self.assertTrue(board.is_empty_cell(test_board, (0, 0)))
        board.place_piece(test_board, (2, 2), False)
        self.assertTrue(test_board[2][2] == 'O')
        board.place_piece(test_board, (2, 2), True)
        self.assertTrue(test_board[2][2] == 'X')
        board.remove_piece(test_board, (2, 2))
        self.assertTrue(board.is_empty_cell(test_board, (2, 2)))

    def test_check_win(self):
        test_board = [['X', 'O', 'O'], ['O', 'X', 'X'], [' ', 'X', ' ']]
        board.place_piece(test_board, (2, 2), True)
        self.assertTrue(board.check_win(test_board, (2, 2), True))
        self.assertFalse(board.check_win(test_board, (2, 2), False))
        board.remove_piece(test_board, (2, 2))
        board.place_piece(test_board, (2, 0), False)
        self.assertFalse(board.check_win(test_board, (2, 0), True))
        self.assertFalse(board.check_win(test_board, (2, 0), False))
        board.place_piece(test_board, (1, 0), True)
        board.place_piece(test_board, (1, 1), False)
        self.assertFalse(board.check_win(test_board, (1, 1), True))
        self.assertTrue(board.check_win(test_board, (1, 1), False))
        # impossible scenario in the actual game (both players win)
        board.place_piece(test_board, (2, 0), True)
        board.place_piece(test_board, (2, 1), False)
        self.assertTrue(board.check_win(test_board, (2, 0), True))
        self.assertTrue(board.check_win(test_board, (2, 1), False))

    def test_possible_moves(self):
        test_board_empty = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        test_board_full = [['X', 'O', 'O'], ['O', 'X', 'X'], ['X', 'X', '0']]
        test_board_mostly = [['X', 'O', 'O'], ['O', 'X', 'X'], [' ', 'X', ' ']]
        possible_moves_empty = [(0, 0), (0, 1), (0, 2), (
            1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        possible_moves_full = []
        possible_moves_mostly = [(2, 0), (2, 2)]
        self.assertEquals(possible_moves_empty,
                          board.possible_moves(test_board_empty))
        self.assertEquals(possible_moves_full,
                          board.possible_moves(test_board_full))
        self.assertEquals(possible_moves_mostly,
                          board.possible_moves(test_board_mostly))


if __name__ == "__main__":
    unittest.main()
