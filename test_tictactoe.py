import unittest
import numpy as np
from tictactoe import find_row, find_column, is_full, is_avaliable, make_mark

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        """Set up a sample game board for tests."""
        self.board = np.array([[' ', 'X', ' '],
                               ['O', 'X', 'O'],
                               [' ', ' ', 'X']])

    # Test for find_row function
    def test_find_row(self):
        self.assertEqual(find_row(1), 0)  # Top row
        self.assertEqual(find_row(5), 1)  # Middle row
        self.assertEqual(find_row(9), 2)  # Bottom row

    # Test for find_column function
    def test_find_column(self):
        self.assertEqual(find_column(1), 0)  # Column 0
        self.assertEqual(find_column(5), 1)  # Column 1
        self.assertEqual(find_column(9), 2)  # Column 2

    # Test for is_full function
    def test_is_full(self):
        full_board = np.array([['X', 'O', 'X'],
                               ['O', 'X', 'O'],
                               ['X', 'O', 'X']])
        empty_board = np.array([[' ', ' ', ' '],
                                [' ', ' ', ' '],
                                [' ', ' ', ' ']])

        self.assertTrue(is_full(full_board))  # Board is full
        self.assertFalse(is_full(empty_board))  # Board is empty
        self.assertFalse(is_full(self.board))  # Partially filled board

    # Test for is_avaliable function
    def test_is_avaliable(self):
        self.assertTrue(is_avaliable(self.board, 0, 0))  # Empty slot
        self.assertFalse(is_avaliable(self.board, 0, 1))  # Already marked slot'
        self.assertFalse(is_avaliable(self.board, -1, 0))  # Negative row - edge case
        self.assertFalse(is_avaliable(self.board, 3, 3))  # Out-of-range indices - edge case
        

    # Test for make_mark function
    def test_make_mark(self):
        make_mark(self.board, 0, 0, 'X')  # Mark empty slot
        self.assertEqual(self.board[0, 0], 'X')  # Check mark was made
        

       

# Run the tests
unittest.main(argv=[''], verbosity=2, exit=False)