from tictactoe import tictactoe # Import the parent class
import random

class InteractiveTicTacToe(TicTacToe):
    def __init__(self):
        super().__init__()  # Call Parent's __init__()
        
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

def main():
    game = InteractiveTicTacToe()
    game.play_game()
    
if __name__ == "__main__":
    main()
           
    
