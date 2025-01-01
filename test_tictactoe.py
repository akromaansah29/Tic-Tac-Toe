import unittest
import numpy as np
from TestableTicTacToe import TestableTicTacToe

class test_tictactoe(unittest.TestCase):

    def setUp(self):
        """Set up a sample game board for tests."""
        predefined_moves =[(0,0), (1,1), (2,2)]
        self.game = TestableTicTacToe(predefined_moves = predefined_moves)
        self.board = np.array([[' ', 'X', ' '],
                               ['O', 'X', 'O'],
                               [' ', ' ', 'X']])
        self.game.board = self.board

    # Test for find_row function
    def test_find_row(self):
        """Test find_row with valid inputs."""
        self.assertEqual(self.game.find_row(1), 0)  # Top row
        self.assertEqual(self.game.find_row(5), 1)  # Middle row
        self.assertEqual(self.game.find_row(9), 2)  # Bottom row

    # Test for find_column function
    def test_find_column(self):
        """Test find_column with valid inputs."""
        self.assertEqual(self.game.find_column(1), 0)  # Column 0
        self.assertEqual(self.game.find_column(5), 1)  # Column 1
        self.assertEqual(self.game.find_column(9), 2)  # Column 2
        
    
    def test_find_column_invalid_inputs(self):
        """Test find_column with invalid inputs (edge cases)."""
        with self.assertRaises(ValueError):
            self.game.find_column(0)  # Invalid input: below valid range
        with self.assertRaises(ValueError):
            self.game.find_column(12)  # Invalid input: above valid range
        
    def test_find_row_edge_cases(self):
        with self.assertRaises(ValueError):
            self.game.find_row(0)  # Input too low
        with self.assertRaises(ValueError):
            self.game.find_row(-5)  # Negative input
        with self.assertRaises(ValueError):
            self.game.find_row(10)  # Input too high  
            
    def test_is_full(self):
        full_board = np.array([['X', 'O', 'X'],
                               ['O', 'X', 'O'],
                               ['X', 'O', 'X']])
        empty_board = np.array([[' ', ' ', ' '],
                                [' ', ' ', ' '],
                                [' ', ' ', ' ']])

        self.assertTrue(self.game.is_full(board = full_board))  # Board is full
        self.assertFalse(self.game.is_full(board = empty_board))  # Board is empty
        self.assertFalse(self.game.is_full())  # Partially filled board 
        
    def test_is_avaliable(self):
        self.assertTrue(self.game.is_available(0, 0))  # Empty slot
        self.assertFalse(self.game.is_available(0, 1))  # Already marked slot'
        self.assertFalse(self.game.is_available(-1, 0))  # Negative row - edge case
        self.assertFalse(self.game.is_available(3, 3))  # Out-of-range indices - edge case
        
    def test_make_mark(self):
        self.game.make_mark(0, 0, 'X')  # Mark empty slot
        self.assertEqual(self.board[0, 0], 'X')  # Check mark was made
        
        # attempting to mark an already occupied slot. it shouldn't be allowed. (edge case)
        self.game.make_mark(0, 1, 'O')  # Try to overwrite slot with 'X'
        self.assertNotEqual(self.board[0, 1], 'O')  # Slot should remain 'X'
        self.assertEqual(self.board[0, 1], 'X')  # check that it didn't change
        
    unittest.main(argv=[''], verbosity=2, exit=False)
        
