import numpy as np
import random


class TicTacToe:
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

    def find_column(self, number):
        """Find the column corresponding to the player's choice."""
        col_map = {1: 0, 4: 0, 7: 0,
                   2: 1, 5: 1, 8: 1,
                   3: 2, 6: 2, 9: 2}
        return col_map.get(number, -1)

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
       
       


    def play_turn(self, choice, mark):
        """Play a turn for the given mark."""
        row = self.find_row(choice)
        col = self.find_column(choice)
        if self.make_mark(row, col, mark):
            return self.possible_termination(mark)
        print(f"Slot {choice} is not available. Try again.")
        return False

    def validate_playerChoice(self):
        
        player_choice = input('Pick an open slot:') 
        while not(int(player_choice) >= 1 and int(player_choice) <= 9):
            print("That's not an open slot.")
            self.display_current_board()
            player_choice = input('Pick an open slot: ')
            
        row = self.find_row(int(player_choice))    
        col = self.find_column(int(player_choice))

        while self.is_available(row,col) == False:
            print("That's not an open slot.")
            self.display_current_board()
            player_choice = input('Pick an open slot: ')
            row = self.find_row(int(player_choice))    
            col = self.find_column(int(player_choice))
           
        self.playerChoice = [row,col]
        
        

    def play_game(self):
        """Main interactive game logic."""
        print('Welcome to Tic Tac Toe!')
        print('===================================')
        if self.first_play == 'H':
            print('You go first. Your letter is X.') 
        else:
            computer_choice = random.randint(1,9)
            row = self.find_row(computer_choice)
            column = self.find_column(computer_choice)
            self.make_mark(row,column,'O')
            
        while self.game_over  == False:
           
           if self.is_full() == False:
                self.display_current_board()   
                self.validate_playerChoice()
                choice  = self.playerChoice
                self.make_mark(choice[0],choice[1],'X') 
                self.possible_termination('X')
                if self.game_over == False:
                    computer_choice = random.randint(1,9)
                    row = self.find_row(computer_choice)
                    col = self.find_column(computer_choice)
                    while self.is_available(row,col) == False:
                        computer_choice = random.randint(1,9)
                        row = self.find_row(computer_choice)
                        col = self.find_column(computer_choice)
                    self.make_mark(row,col,'O')
                    self.possible_termination('O')
           else:
                print('Tie')
                print('Play again? Press Enter to play again.')   
                print('\n')
                print('**END OF PROGRAMMING**')   
                self.game_over = True
           
           

 
            



# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
