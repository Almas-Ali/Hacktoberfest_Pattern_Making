# Tic-Tac-Toe Game

# To display the board
def display_board(board):
    print(board[7] +'|'+board[8]+'|'+board[9])
    print(board[4] +'|'+board[5]+'|'+board[6])
    print(board[1] +'|'+board[2]+'|'+board[3])
    
# To check for each players marker
def player_input():
    ask=True
    while(ask):
        player1 = input('Player 1, What is your Marker? : ')
        if player1 == 'X':
            player2='O'
            print('Player 2 your marker is O')
            ask=False
        elif player1=='O':
            player2='X'
            print('Player 2 your marker is X')
            ask=False
        else:
            print('Please choose the marker as X or O')
    return (player1,player2)

# To place the marker at desired location
def place_marker(board, marker, position):
    board[position]=marker
    return board

# To check if the player wins
def win_check(board, mark):
    if mark in board[1] and mark in board[2] and mark in board[3]:
        return True
    elif mark in board[4] and mark in board[5] and mark in board[6]:
        return True
    elif mark in board[9] and mark in board[8] and mark in board[7]:
        return True
    elif mark in board[1] and mark in board[4] and mark in board[7]:
        return True
    elif mark in board[2] and mark in board[5] and mark in board[8]:
        return True
    elif mark in board[3] and mark in board[6] and mark in board[9]:
        return True
    elif mark in board[1] and mark in board[5] and mark in board[9]:
        return True
    elif mark in board[3] and mark in board[5] and mark in board[7]:
        return True
    return False

# To randomly choose which player starts the game
import random
def choose_first():
    if random.randint(0,1)==0:
        return 'player2'
    else:
        return 'player1'

# To check if position entered is empty 
def space_check(board, position):
    return board[position]==' '
    
# To check if the board is full
def full_board_check(board):
    return ' ' not in board
    
# To return valid position
def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Enter your position: '))
    return position

# To check the replay of the game    
def replay():
    replay = input('Do you want to play again?\nYes or No: ')
    return replay.lower()=='yes'

# Code
print('Welcome to Tic Tac Toe!')
while True:
    real_board = [' ']*10
    real_board[0] = '$'
    display_board(real_board)
    player1, player2 = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    gameon=True
    while gameon:
        if turn == 'player1':
            position = player_choice(real_board)
            place_marker(real_board, player1, position)
            display_board(real_board)
            if win_check(real_board,player1):
                print('Player 1 Won!!!')
                gameon=False
            elif full_board_check(real_board):
                print('Game Drawn')
                gameon=False
            else:
                turn='player2'
        else:
            position = player_choice(real_board)
            place_marker(real_board, player2, position)
            display_board(real_board)
            if win_check(real_board,player2):
                print('Player 2 Won!!!')
                gameon=False
            elif full_board_check(real_board):
                print('Game Drawn')
                gameon=False
            else:
                turn='player1'
    if not replay():
        print('Thank You! for playing')
        break



