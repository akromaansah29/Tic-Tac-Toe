class TestableTicTacToe(TicTacToe):
    def __init__(self, predefined_moves):
        super().__init__()
        self.predefined_moves = predefined_moves
        self.move_index = 0

    def get_next_move(self):
        """Retrieve the next predefined move."""
        if self.move_index < len(self.predefined_moves):
            move = self.predefined_moves[self.move_index]
            self.move_index += 1
            return move
        return None

    def play_game(self):
        """Automated game logic for testing."""
        while not self.game_over:
            self.display_current_board()
            player_choice = self.get_next_move()
            if player_choice is None:
                print("No more moves available.")
                break
            print(f"Player {self.current_player} chose: {player_choice}")
            row = self.find_row(player_choice)
            col = self.find_column(player_choice)
            if self.make_mark(row, col, self.current_player):
                if self.possible_termination(self.current_player):
                    print(f"Player {self.current_player} wins!")
                    self.game_over = True
                elif self.is_full():
                    print("It's a tie!")
                    self.game_over = True
                # to ensure both 'X' and 'O'players get a turn after each other  
                if self.current_player == 'X':
                    self.current_player = 'O'
                else:
                    self.current_player = 'X'
            else:
                print("Invalid move.")
