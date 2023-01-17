from IPython.display import clear_output
import random
#Board Display
def board_is(test_board):
    clear_output()
    print( ' ' +'|' + ' '+'|'+' ')
    print(test_board[7] + '|' + test_board[8]+'|'+test_board[9])
    print( ' ' +'|' + ' '+'|'+' ')
    print('------')
    print(test_board[4] + '|' + test_board[5]+'|'+test_board[6])
    print( ' ' +'|' + ' '+'|'+' ')
    print('------')
    print(test_board[1] + '|' + test_board[2]+'|'+test_board[3])
    print( ' ' +'|' + ' '+'|'+' ')
    
test_board = ['#','X','O','X',' ','O','O','X','O','X']
#board_is(test_board)
#Option to choose the player to choose their markers 
def user_marker():
    a = ['X','O']
    choice = 'L'
    while choice not in a:
        choice = input("Choose a marker ('X' or 'O') : ").upper()
        if choice not in a:
            print("choose a appropriate marker !")
            
    if choice =='X':
        return ('X','O')
    else:
        return ('O','X')
    #to check the enterd postion in the board is empty or not
def check_space(test_board,postion):
    return test_board[postion] == ' '
#to check the whole board is full or not
def chech_full__board(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True
def player_choice(board):#optio to the player to choose the postion to enter the marker
    postion = 0
    while postion not in [1,2,3,4,5,6,7,8,9] or not check_space(board,postion):
        postion = int(input("ENter a postion (1 - 9) : "))
    return postion
    
#Now checking whether the the player at the turn win or not
def win_check(board,mark):
   return(( board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
   #to choose the player randomly from the two players
def player_turn():
    a = random.randint(0,1)
    if a==1:
        return 'Player1'
    else:
        return 'Player2'    
#to insert the marker into the board 
def place_marker(board,postion,marker):
       board[postion] = marker
#he want to play again or not
def play_again():
    y = 'se'
    while y in ['y','n']:
        y  = input("Enter your choice (y or n) : ").lower()
    if y =='y':
        return True
    else:
        return False
#Entering into the game 

def game_in(test_board):
    print("Welcome to Tic - Toc - Toe game designed by sekhar")
    again = True
    while again:
        test_board = [' '] *10
        #player choice
        player1,player2= user_marker()
        #to know the player turn 
        a  = player_turn()
        if a=='Player1':
            print( a + " go first")
        else:
            print(a + " go first")
        ready = input("Are you ready  (y or n)  ?").lower()
        if ready =='y':
             game_on = True
        else:
            game_on = False
        while game_on:
            if a == 'Player1':
                board_is(test_board)
                position = player_choice(test_board)
                place_marker(test_board,position,player1)
                if win_check(test_board,player1):
                    board_is(test_board)
                    print("Player 1 Has Won the game")
                    print("Better next Time To Player 2 !!")
                    game_on = False
                else:
                   if chech_full__board(test_board):
                       board_is(test_board)
                       print("Game Has been Tied !")
                       print("Better time next !")
                       break
                
                   else:
                         a = 'Player2'
            
            else:
                 board_is(test_board)
                 position = player_choice(test_board)
                 place_marker(test_board,position,player2)
                 if win_check(test_board,player2):
                     board_is(test_board)
                     print("Player 2 Has Won the game")
                     print("Next time better to Player 1 !!")
                     game_on = False
                 else:
                     if chech_full__board(test_board):
                          board_is(test_board)
                          print("Game Has been Tied !")
                          print("Better time next !")
                          break
                
                     else:
                         a = 'Player1'
        print("I am sekhar !")
        if not play_again():
            return True
        else:
            return False
        pass
        print("I learning python progrmaing ! ")
            #return True
        #else:
         #   return False
    
game_in(test_board)          
               
                         
                
                  
                
                
            
            
            
    
    
    
    


        