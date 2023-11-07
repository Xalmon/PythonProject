import unittest
from Tic_tac_package.Board import Board


class TestBoard(unittest.TestCase):
    def test_that_board_exist_and_init(self):
        board = Board()
        self.assertEqual(board.board_state, [" "] * 9)

    def test_if_position_is_empty(self):
        board = Board()
        self.assertTrue(board.empty_board(0))
        self.assertTrue(board.empty_board(4))
        self.assertTrue(board.empty_board(8))
        self.assertTrue(board.empty_board(1))
        self.assertTrue(board.empty_board(2))

    def test_that_board_is_full(self):
        board = Board()
        self.assertFalse(board.full_board())
        board.board_state = ["X", "O", "X", "O", "X", "X", "X", "O", "X"]
        self.assertTrue(board.full_board())

    def test_that_you_can_make_move(self):
        board = Board()
        self.assertTrue(board.make_move(0, "X"))
        self.assertFalse(board.make_move(0, "O"))
        self.assertTrue(board.make_move(4, "O"))

    def test_that_you_can_check_winner(self):
        board = Board()
        board.board_state = ["X", "X", "X", "O", "O", " ", " ", " ", " "]
        self.assertTrue(board.check_winner("X"))
        board.board_state = ["O", "X", "X", "O", "O", "X", "X", "O", "X"]
        self.assertTrue(board.check_winner("X"))


if __name__ == '__main__':
    unittest.main()
