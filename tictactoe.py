import sys
# GitHub Actions or automated testing environments can’t handle dynamic user inputs. We’ll need to replace input() with a mockable or test-safe alternative
import numpy as np
import random
# each number represents a certain column
col_0=[1,4,7]
col_1=[2,5,8]
col_2=[3,6,9]


# Wrapper for safe input
def safe_input(prompt):
    """Wrapper around input() to safely handle testing environments."""
    if 'unittest' in sys.modules:
        return '1'  # Default value during tests
    else:
        return input(prompt)

def is_full(array):
    #Parameters
    #----------
    #array : array you want to check if it's full
    #Returns
    #-------
    #boolean
    if (len(array[array == ' ']) == 0):
        return True
    else:
        return False
    
    
    

def find_row(number):
    #Parameters
    #----------
    #number : user's input(between 1 and 9) to be used to find a row in the matrix(array)
    #Returns
    #-------
    #int
    
    if number >= 1 and number <= 3:
        return 0
    elif number >=4 and number <= 6:
        return 1
    elif number >=7 and number <= 9:
        return 2
   

def find_column(number):
    #Parameters
    #----------
    #number : user's input(between 1 and 9) to be used to find a row in the matrix(array)
    #Returns
    #-------
    #int
    
    if number in col_0:
        return 0
    elif number in col_1:
        return 1
    elif number in col_2:
        return 2
    


# make sure you check if row and column are valid
def is_avaliable(array, row, column):
    # Check for out-of-bounds indices, shape[0] = rows of array in numpy and shapes[1]=columns of array on numpy
    if row < 0 or row >= array.shape[0] or column < 0 or column >= array.shape[1]:
        return False
    
    # Check slot availability
    return array[row, column] == ' '

    
def make_mark(array,row,column,mark):
    #Parameters
    #----------
    #array : array you want to make a mark in
    #row : the row of choice
    #column : the column of choice
    #mark : mark is either X or O where X represents player  and O represents computer
    if row < 0 or row >= array.shape[0] or column < 0 or column >= array.shape[1]:
        return  # Do nothing if out of bounds
    array[row][column] = mark
    

def display_initial_board():
    #no parameters
    
    print('   |   |    ')
    print('---+---+----')
    print('   |   |    ')
    print('---+---+----')
    print('   |   |    ')
    

# displays board with updated array values in their rightful positions
def display_current_board(array):
    #Parameters
    #----------
    #array : array you want to display
    
    print(' {} | {} | {}'.format(array[0][0],array[0][1],array[0][2]))
    print('---+---+----')
    print(' {} | {} | {}'.format(array[1][0],array[1][1],array[1][2]))
    print('---+---+----')
    print(' {} | {} | {}'.format(array[2][0],array[2][1],array[2][2]))
    

    
def diagonal_win(array,mark):
    #Parameters
    #----------
    #array : array you want to check for a diagonal win
    #mark : mark is either X or O where X represents player  and O represents computer
    #Returns
    #----------
    #Boolean
    
    if (array[0][0] == array[1][1]==array[2,2]) or (array[2,0] == array[1,1] == array[0,2]):
        if array[1,1] == mark: #use common factor to compare
            return True
    
    return False

    
def horizontal_win(array,mark):
    #Parameters
    #----------
    #array : array you want to check for a horizontal win
    #mark : mark is either X or O where X represents player  and O represents computer
    #Returns
    #----------
    #Boolean
    
    for i in range(3): # i representing row
        j = 0
        if (array[i,j] == array[i,j+1] == array[i,j+2]== mark):   
            return True
    return False
            
def vertical_win(array,mark):
    #Parameters
    #----------
    #array : array you want to check for a vertical win
    #mark : mark is either X or O where X represents player  and O represents computer
    #Returns
    #----------
    #Boolean
    
     for j in range(3): # j representing column
        i = 0
        if (array[i,j] == array[i+1,j] == array[i+2,j]):
            if array[i,j] == mark:   
                return True
     return False
            
            
def possible_termination(array,mark):
    #Parameters
    #----------
    #array : array you want to check for a possible win or loss which would lead to termination
    #mark : mark is either X or O where X represents player  and O represents computer
    #Returns
    #----------
    #Boolean
    
       if diagonal_win(array,mark) == True: 
            if mark == 'X':
                display_current_board(array)
                print('\n')
                print('You win! Game Over!')
            elif mark == 'O':
                display_current_board(array)
                print('\n')
                print('You lose!')
            print('Play again? Press Enter to play again. ') 
            print('\n')
            print('**END OF PROGRAMMING**') 
                 
            return True    
                
       elif horizontal_win(array,mark) == True:
            if mark == 'X':
                display_current_board(array)
                print('\n')
                print('You win! Game Over!')
            elif mark == 'O':
                display_current_board(array)    # i wanted the player to see the board after the loss.(to see exactly what happened)
                print('\n')
                print('You lose!')
            print('Play again? Press Enter to play again. ') 
            print('\n')
            print('**END OF PROGRAMMING**')     
            return True  
            
       elif vertical_win(array,mark) == True:
            if mark == 'X':
                display_current_board(array)
                print('\n')
                print('You win! Game Over!')
            elif mark == 'O':
                display_current_board(array)
                print('\n')
                print('You lose!')
            print('Play again? Press Enter to play again. ') 
            print('\n')
            print('**END OF PROGRAMMING**')     
            return True  
        
       else:
            return False
       
       
    
    
    
    
print('Welcome to the tick tak toe Game') 
print('===================================')
game_over = False
arry = np.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
coin_flip = ['H','T'] #coin flip to select who plays first
first_play = random.choice(coin_flip)

if first_play == 'H':
    print('You go first. Your letter is X.') 

    
else:
    
    
    computer_choice = random.randint(1,9)
    row = find_row(computer_choice)
    column = find_column(computer_choice)
    make_mark(arry,row,column,'O')

    
while game_over == False:
    
        if is_full(arry) == False:
            display_current_board(arry)   
            player_choice = safe_input('Pick an open slot: ')
            
            while not(int(player_choice) >= 1 and int(player_choice) <= 9):
                print("That's not an open slot.")
                display_current_board(arry)
                player_choice = safe_input('Pick an open slot: ')
                
        
            row = find_row(int(player_choice))    
            col = find_column(int(player_choice))
        
            while is_avaliable(arry,row,col) == False:
                print("That's not an open slot.")
                display_current_board(arry)
                player_choice = safe_input('Pick an open slot: ')
                row = find_row(int(player_choice))    
                col = find_column(int(player_choice))
                
            make_mark(arry,row,col,'X') 
            game_over = possible_termination(arry,'X')
            
            if game_over == False:
                
                computer_choice = random.randint(1,9)
                row = find_row(computer_choice)
                col = find_column(computer_choice)
                
                while is_avaliable(arry,row,col) == False:
                    computer_choice = random.randint(1,9)
                    row = find_row(computer_choice)
                    col = find_column(computer_choice)
                    
               
                make_mark(arry,row,col,'O')
                game_over = possible_termination(arry,'O')
                
        else:
             print('Tie')
             print('Play again? Press Enter to play again.')   
             print('\n')
             print('**END OF PROGRAMMING**')   
             game_over = True

     
    
