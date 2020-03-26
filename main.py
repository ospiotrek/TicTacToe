##Ogolnie to wszystko jest pomieszane w caly swiat##
#####Plansza
board =['-', '-', '-', '-', '-', '-', '-', '-', '-']
  
def show_board():
     print('(1|2|3)\n(4|5|6)\n(7|8|9)\n') 
     print(board[0] + '|' + board[1] + '|' + board[2])
     print(board[3] + '|' + board[4] + '|' + board[5])
     print(board[6] + '|' + board[7] + '|' + board[8] + '\n')
     
#######wstawianie X
def x_number():
     x_number = input("Choose a number 1-9:")
     x_number = int(x_number) - 1
     if x_number in range(0, 9):
          board[x_number] = 'X'
          show_board()
          print("Player_O's turn\n")
          o_turn()
     else:
          show_board()
          print('invalid input\n')
          rpt_xnumber()
          

######wstawianie O
def o_number():
     o_number = input("Choose a number 1-9:")
     o_number = int(o_number) - 1
     if o_number in range(0, 9):
          board[o_number] = 'O'
          show_board()
          print("Player_X's turn\n")
          x_turn()
     else:          
          show_board()
          print('invalid input\n')
          rpt_onumber()
          
####powtorz jesli invalid input (nie wiem czemu ale tak dziala a inaczej nie chce)
def rpt_xnumber():
     x_number()
def rpt_onumber():
     o_number()

#####Tura gracza X
def x_turn():
     x_number1 = input("Choose a number 1-9:")
     x_number1 = int(x_number1) - 1
     if x_number1 in range(0, 9):
          if board[x_number1] == '-':
               board[x_number1] = 'X'
               show_board()
               check_game_X()
          else:
               show_board()
               print('invalid input\n')
               x_turn()
     else:
          show_board()
          print('invalid input\n')
          x_turn()

####Tura gracza O
def o_turn():
     o_number1 = input("Choose a number 1-9:")
     o_number1 = int(o_number1) - 1
     if o_number1 in range(0, 9):
          if board[o_number1] == '-':
               board[o_number1] = 'O'
               show_board()
               check_game_O()
          else:
               show_board()
               print('invalid input\n')
               o_turn()
     else:
          show_board()
          print('invalid input\n')
          o_turn()

##############Sprawdzanie rezultatu###########
######Sprawdz gdy tura gracza X
def check_game_X():
    w1 = board[0] + board[1] + board[2] 
    w2 = board[3] + board[4] + board[5] 
    w3 = board[6] + board[7] + board[8] 
    k1 = board[0] + board[3] + board[6] 
    k2 = board[1] + board[4] + board[7] 
    k3 = board[2] + board[5] + board[8] 
    s1 = board[0] + board[4] + board[8] 
    s2 = board[2] + board[4] + board[6]  
    if w1 == 'XXX' or w2 =="XXX"or w3 =="XXX" or k1 =="XXX" or k2 =="XXX" or k3 =="XXX" or s1 =="XXX" or s2 =="XXX":
        print('Player_X is a winner')
    elif '-' not in board:
        print('Draw')
    else:
        print("Player_O's turn\n")
        o_turn()

#####Sprawdz gdy tura gracza O        
def check_game_O():
    w1 = board[0] + board[1] + board[2] 
    w2 = board[3] + board[4] + board[5] 
    w3 = board[6] + board[7] + board[8] 
    k1 = board[0] + board[3] + board[6] 
    k2 = board[1] + board[4] + board[7] 
    k3 = board[2] + board[5] + board[8] 
    s1 = board[0] + board[4] + board[8] 
    s2 = board[2] + board[4] + board[6] 
    if w1 == 'OOO' or w2 =="OOO"or w3 =="OOO" or k1 =="OOO" or k2 =="OOO" or k3 =="OOO" or s1 =="OOO" or s2 =="OOO":
        print('Player_O is a winner')
    elif '-' not in board:
        print('Draw')
    else:
        print("Player_X's turn\n")
        x_turn()

#####rozpoczynanie gry
def play_a_game():
    show_board()
    player_list = ['Player_X','Player_O']
    import random
    chosen_player = random.choice(player_list)
    print(chosen_player + ' begins\n')
    if chosen_player == player_list[0]: 
         x_number()
    else:
         o_number()



play_a_game()







