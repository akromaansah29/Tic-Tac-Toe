import numpy as np
class tictactoe:
    def __init__(self):
        """Initialize the game with an empty board and game state."""
        self.board = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
        self.playerChoice = [None,None]
        self.game_over = False
        self.current_player = 'X'  # Default player is 'X'
        self.coin_flip = ['H', 'T']
        self.first_play = random.choice(self.coin_flip)

    def is_full(self):
        """Check if the board is full."""
        return len(self.board[self.board == ' ']) == 0

    def find_row(self, number):
        """Find the row corresponding to the player's choice."""
        if 1 <= number <= 3:
            return 0
        elif 4 <= number <= 6:
            return 1
        elif 7 <= number <= 9:
            return 2
        else:
            raise ValueError(f"Invalid input: {number}. Please enter a number between 1 and 9.")
            

    def find_column(self, number):
        """Find the column corresponding to the player's choice."""
        col_map = {1: 0, 4: 0, 7: 0,
                   2: 1, 5: 1, 8: 1,
                   3: 2, 6: 2, 9: 2}
        if number not in col_map:
            raise ValueError(f"Invalid input: {number}. Please enter a number between 1 and 9.")
        return col_map[number]

    def is_available(self, row, col):
        """Check if a slot is available."""
        return self.board[row, col] == ' '

    def make_mark(self, row, col, mark):
        """Place a mark on the board."""
        if self.is_available(row, col):
            self.board[row, col] = mark
            return True
        return False

    def display_current_board(self):
        """Display the current game board."""
        print(' {} | {} | {}'.format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print('---+---+---')
        print(' {} | {} | {}'.format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print('---+---+---')
        print(' {} | {} | {}'.format(self.board[2][0], self.board[2][1], self.board[2][2]))

    def diagonal_win(self, mark):
        """Check for a diagonal win."""
        return (self.board[0, 0] == self.board[1, 1] == self.board[2, 2] == mark or
                self.board[2, 0] == self.board[1, 1] == self.board[0, 2] == mark)

    def horizontal_win(self, mark):
        """Check for a horizontal win."""
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2] == mark:
                return True
        return False

    def vertical_win(self, mark):
        """Check for a vertical win."""
        for j in range(3):
            if self.board[0, j] == self.board[1, j] == self.board[2, j] == mark:
                return True
        return False

    def possible_termination(self, mark):
        if self.diagonal_win(mark) == True or self.horizontal_win(mark) == True or self.vertical_win(mark) : 
            if mark == 'X':
                self.display_current_board()
                print('\n')
                print('You win! Game Over!')
            elif mark == 'O':
                self.display_current_board()
                print('\n')
                print('You lose!')
            print('Play again? Press Enter to play again. ') 
            print('\n')
            print('**END OF PROGRAMMING**') 
            self.game_over = True
       
       
